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
