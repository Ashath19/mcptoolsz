# -------------------------------------------------------------------------------------------
#  Copyright (c) 2024.  SupportVectors AI Lab
#
#  This code is part of the training material, and therefore part of the intellectual property.
#  It may not be reused or shared without the explicit, written permission of SupportVectors.
#
#  Use is limited to the duration and purpose of the training at SupportVectors.
#
#  Author: SupportVectors AI Training
# -------------------------------------------------------------------------------------------

"""
Newsletter MCP Server

This module builds an MCP (Model Context Protocol) server using the FastMCP v2 library.
The server provides various tools for news aggregation and basic operations.

Available Tools:
- addition: Add two numbers together
- serper_search: Fetch recent news articles using the Serper API
- mediastack_search: Fetch recent news articles using the MediaStack API

Usage:
    To call tools from a client, send HTTP POST requests to the server's endpoints:
    - http://127.0.0.1:9000/mcp/addition=
    - http://127.0.0.1:9000/mcp/serper_search  
    - http://127.0.0.1:9000/mcp/mediastack_search

    Each endpoint expects a JSON payload with the required parameters.

For more details, refer to the FastMCP documentation: https://gofastmcp.com/clients/client
"""

from typing import Dict, Any

from fastmcp import FastMCP
from openai_agents.mcp.tools.serper_tool import fetch_serper_news
from openai_agents.mcp.tools.add_tool import add

# Initialize the MCP server
mcp = FastMCP(name="newsletter-mcp-server")


@mcp.tool()
def addition(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a (int): First number to add
        b (int): Second number to add
        
    Returns:
        int: The sum of a and b
    """
    return add(a, b)


@mcp.tool()
def serper_search(query: str) -> Dict[str, Any]:
    """
    Fetch recent news articles using the Serper API for a given query.
    
    This tool performs a Google search via Serper API and returns the raw search results
    including news articles, web results, and other relevant information.
    
    Args:
        query (str): Search query string (e.g., "artificial intelligence news")
        
    Returns:
        Dict[str, Any]: Raw JSON response from Serper API containing search results
    """
    return fetch_serper_news(query)

def main():
    """
    Start the MCP server.
    
    The server will run on http://127.0.0.1:9000 and expose all registered tools
    as HTTP endpoints under the /mcp/ prefix.
    """
    mcp.run(transport="http", host="127.0.0.1", port=9000)


if __name__ == "__main__":
    main()