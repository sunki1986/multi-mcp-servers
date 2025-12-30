from fastmcp import FastMCP
import asyncio 
from dotenv import load_dotenv
import os
load_dotenv()

math_mcp=os.getenv('mcp_server_math')
math_science=os.getenv('mcp_server_science')

proxy_1=FastMCP.as_proxy(math_mcp)
proxy_2=FastMCP.as_proxy(math_science)


mcp_sentinal= FastMCP(name='main_server')

mcp_sentinal.mount(proxy_1)
mcp_sentinal.mount(proxy_2)


asyncio.run (mcp_sentinal.run_http_async(transport="streamable-http",host="0.0.0.0",port=8000,stateless_http=True))

