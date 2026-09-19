# Week 6 Summary
**Resource**: 
- https://github.com/ed-donner/agents
- https://drive.google.com/drive/folders/1AM4h33TahM2dccriRRaH32roi03UYOZv
- https://openai.github.io/openai-agents-python/mcp/
- https://www.philschmid.de/context-engineering
- https://www.tavily.com/
- https://www.massive.com


**SEP 12,2026**
## An Agent
- It is the LLM which has tools in a loop to achieve a goal
- Or Ann LLM in the Harness -> Agent Harness is all the tools that surrounded around the LLM to achieve the goal

from low-level to high level framework
- low-level: LangChain-Core and LangGraph
- High-level: Claude Agent SDK

## MCP (Model Context Protocol)
### What it is not:
- A framework for building agent
- A fundemental change to how agents work
- A way to code agent

### What it is:
- A protocol - a standard
- A simple way to integrate tools, reources, prompts
- "A USB-C port for AI applications"

**note**: 
- MCP is all about connectivity and standard
- Standards covers three things: tools, resources, and prompt
- Only tool is more popular not the other resources and in practice we just use MCP for a tool

**Reasons not to be excited:**
- It’s just a standard, it’s not tools themselves
- LangChain already has a big Tools ecosystem
- You can already make any function into a Tool

**Reason to be excited**
- Makes it frictionless to integrate
- Huge ecosystem
- Agreed standards are important -> It comes from Anthropic and widely addopted and handed over to foundation called it agentic AI foundation which rolls up to the Linux foundation

## MCP Core Concepts
The Three Components:
- Host is an LLM app like Claude or our Agentic Platform -> it is like chatgpt, harness running on it
- MCP Client lives inside Host and connects 1:1 to MCP Server
- MCP Server provides tools, context and prompts -> It has some standardized code to describe tools using the json description tools showning what are the parameters, args, and describe about the parameters -> They are list tools and call tools
    - Server has two imoprtant jobs: 1. list the MCP tools and 2. calling toolss

**Note**:
- MCP server mpst often runs in your box - you are downloading MCP and running locally and the MCP job is to describe API in english for LLM model
- Look at context 7 -> https://context7.com/ & https://cursor.com/marketplace/upstash
- The communication is happening by Transport mechanisms:
    - Stdio spawning a process and communicates via standard input/output
    - while Streamable HTTP uses HTTP (replaces the older SSE)

### Connecting to MCP servers
A server is just a set of parameters
- STDIO (Local): a local process to spawn
    - fetch: {"command": "uvx", "args": ["mcp-server-fetch"]} -> python program (run the uvx and the mcp-server-fetch package)
    - playwright: {"command": "npx", "args": ["@playwright/mcp@latest"]} -> javascript program

- Streamable HTTP (a remote URL):
    - context7: {"url": "https://mcp.context7.com/mcp", "timeout": 60}

### Spawning a local server
- uvx: for Python MCP servers
- npx: for Node and JavaScript servers
- docker: for servers packaged as a container

### Why make an MCP Server
- Allow others to incorporate tools
- Consistently incorporate all our MCP Servers
- Understand the plumbing

### Reasons not to make an MCP Server
- If it's only for us, then we could just make tools - the @function_tool decorator can make any function into a tool
    - Because MCP is adding more boundaries which is not neccessary to have in own use

### Number of MCPs
1. Stio call using uvx -> local
2. Stio call using npx -> local
3. Remote Server using streamable HTTP
4. Hosted MCP (Managed MCP) -> Host like OpenAI creates the MCP for you and run and manage the backend infrustructure as a service they provide for you. -> check out https://openai.github.io/openai-agents-python/mcp/ 

**Note from day's 3**
- Rather providing many MCP tools for searching and retrieving the webs, you can connect the search endpoints (Upward level) -> take a leaf of the books the skills which it calls the prograsive disclosure and avoid pollutte the agent and make the agent be more coherent. 

**Note from day's 4**:
- when you creating seperate agents make sure:
    - the context for each agant are independent and we can seperate those from each other
- It is recommanded to sepercate your promots, MCP servers, and tools in diferent modules 







