from fastmcp.server.server import FastMCP
import asyncio
import logging
logging.basicConfig(filename='app.log',level=logging.INFO ,format='%(asctime)s - %(levelname)s - [%(funcName)s():%(lineno)d] - %(message)s')

mcp = FastMCP(name="Math MCP Server", json_response=True, stateless_http=False)

@mcp.tool()
async def add_numbers(a: int, b: int) -> int:
    """addition of two numbers"""
    logging.info('add numbers from math server tool..')
    return a + b

@mcp.tool()
async def multiply_numbers(a: int, b: int) -> int:
    """multiply of two numbers"""
    logging.info('multiply numbers from math server tool..')
    return a * b

async def main():
    await mcp.run_async(transport="streamable-http",host="127.0.0.1",port=8001,path="/mcp")
    # print("customer routes list")
    # print(mcp.custom_route)

if __name__ == "__main__":
    asyncio.run(main())  # Run the async main function
