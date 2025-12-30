# Multi-Server MCP Wrapper

This project implements a unified **Model Context Protocol (MCP)** server that wraps two sub-servers into a single interface. This architectural approach improves maintainability by centralizing configuration and providing a single entry point for LLM clients.

## Features
- **Unified Interface**: Wraps two specialized MCP servers into one for easier deployment.
- **Python-First**: Built with modern Python and managed by [uv](astral.sh) for high-performance dependency management.
- **Simplified Configuration**: Only one server needs to be added to your client config (e.g., Claude Desktop or Cursor).

## Prerequisites
- [uv](docs.astral.sh) installed on your system.
- Python 3.12 or higher.

## Installation

Clone the repository and install dependencies using `uv`:

```bash
git clone <your-repo-url>
cd <your-repo-name>
uv sync
```

## Run

1. python mcp_mapth.py -- run server 1
2. python mcp_science.py -- run server 2
3. python server.py -- main server that wraps both the servers for end use

## Testing

Test using postman by creating a new MCP Collection. 
Steps:
1. Click connect button
2. Run one of the tools listed 
<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/f737c575-37ed-48de-8b43-9b84ea17ed59" />
