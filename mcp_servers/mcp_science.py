from fastmcp.server.server import FastMCP
import asyncio
import logging
logging.basicConfig(filename='app.log',level=logging.INFO ,format='%(asctime)s - %(levelname)s - [%(funcName)s():%(lineno)d] - %(message)s')

mcp = FastMCP(name="Science MCP Server", json_response=True, stateless_http=False)

@mcp.tool()
async def newtons_law(query:str) -> str:
    """Newtons law of action"""
    logging.info('newtons_law from science server tool..')
    return "query:"+query+"\n"+"Answer:Newton's Laws of Motion are three fundamental principles describing the relationship between an object's motion and the forces acting on it"

@mcp.tool()
async def einstein_law(query:str) -> str:
    """Einstein relativity theory"""
    logging.info('einstein_law from science server tool..')
    return "query:"+query+"\n"+"Answer:Einstein's theory of relativity is a two-part theory that changed our understanding of gravity, space, and time"

async def main():
    await mcp.run_async(transport="streamable-http",host="127.0.0.1",port=8002,path="/mcp")

if __name__ == "__main__":
    asyncio.run(main())  # Run the async main function
