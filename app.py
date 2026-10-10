import atexit

import saspy
import streamlit as st


def close_sas_session(sas: saspy.SASsession) -> None:
    if sas.SASpid is None:
        print("SAS session is already closed.", flush=True)
        return
    sas.endsas()

@st.cache_resource
def get_sas_session() -> saspy.SASsession:
    sas = saspy.SASsession()
    # SAS init code to create sample dataset
    sas.submit("""
    proc copy in=sashelp out = work ; 
      select class iris ; 
    run;
    """ 
    )

    atexit.register(close_sas_session, sas)

    return sas

sas = get_sas_session()

LIBREF = "WORK"  
_tables = sas.list_tables(libref=LIBREF)
tables = [item[0] for item in _tables]

# Streamlit UI    
table = st.selectbox(
    f"Select data from {LIBREF}",
    tables,
)

ll = sas.submit(
    f"""
    title1 "10 Obs from {table}" ;
    proc print data = {LIBREF}.{table}(obs=10) ;
    run ;
    """,
    results="HTML",
)

# Display the SAS Result in Streamlit
st.iframe(ll["LST"])