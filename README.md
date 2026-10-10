# SASPy 応用
[2026年のSASユーザー総会](https://sas-user2026.ywstat.jp/program.html)のサンプル用リポジトリ  

SASPyを使った実践的な例として  
- Streamlit による アプリケーション作成 (app.py)
- Fast MCP による MCPサーバー構築 (server.py)

におけるSASPyの使用例を紹介します。

## 実行環境
SASPyについては、接続可能にしておいてください。  
基本的にSASPyは最新にしておき、その他もある程度アップデートされていればそれでも問題ないかと思います。  
uv を使用できる場合は、`uv sync` で、その他環境の場合は、requirements.txt で環境を揃えることはできます。  

## 実行と利用
uvを使用していて、仮想環境が有効になっていない場合は、`uv run`をつけて実行してください。   
MCPサーバーとして実行する場合、使用ツールによって設定ファイルや方法などが違います。  
一般にはコマンドとして、`uv`、引数に`run`、`python`、`server.py`を指定し、作業ディレクトリにプロジェクトのパスを指定することで、コーディングエージェント等から利用できます。

Streamlit: `streamlit run app.py`  
FastMCP: `python server.py`  

## トピックと注意
それぞれで基本的なセッション管理と  
- app.py: HTML形式の実行結果の利用 
- server.py: メタデータの取得、Apache arrow形式の利用、例外処理

のようなトピックを扱っています。  

SASPyを中心にした、最小限のサンプルです。  
StreamlitおよびFastMCPに特有の処理の作り込みなどは各自で行ってください。

## ライセンス
MIT-0（MIT No Attribution）  
チュートリアル的なサンプルコードなので、コードをコピーや改変して使用してもクレジット表記は不要です。