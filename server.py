import saspy
from fastmcp import FastMCP

mcp = FastMCP("Sample MCP Server using SASPy")
sas = None

@mcp.tool
def list_tables(libref: str) -> list:
    """List tables in libref."""
    tables = sas.list_tables(libref=libref, label=True)
    return tables

@mcp.tool
def get_schema(table: str, libref: str) -> str:
    """Get schema for table in libref."""
    ar_table = sas.sd2arrow(table=table, libref=libref)
    schema = ar_table.schema
    # schema = sas.sasdata(table=table, libref=libref).schema(sasattrs=True, xattrs=True)
    return str(schema)

@mcp.tool
def print(table: str, libref: str = "work", obs: int = 5) -> str:
    """Print observation from a SAS dataset."""
    sas.check_error_log = False
    ll = sas.submit(
        f"""
        title ;
        proc print data = {libref}.{table}(obs={obs}) ;
        run ;
        """,
        results="TEXT",
    )
    if sas.check_error_log:
        return ll["LOG"] 
    
    return "Succcessfully printed the dataset."

if __name__ == "__main__":
    sas = saspy.SASsession()
    # SAS init code to create sample dataset
    sas.submit("""
        data work.test_label(label="Test Dataset Label");
            input id name $ age;
            label id = "ID Number" name = "Name" age = "Age";
            datalines;
        1 Alice 25
        2 Bob 30
        3 Carol 28
        ;
        run;

        proc datasets lib=work nolist;
            modify test_label;
            xattr add ds attr="ds attribute" ;
            xattr add var id (attr="var attribute") ;
        quit;
    """
    )
    
    try:
        mcp.run()
    finally:
        sas.endsas()