# Week 4 Summary
**Resource**: 
- https://github.com/ed-donner/agents
- https://drive.google.com/drive/folders/12jSOLymkka2ZPVVuBVavuC5IZTz4mvTK
- https://docs.langchain.com/build-overview
- https://docs.langchain.com/oss/python/deepagents/overview
- https://news.ycombinator.com

**SEP 04,2026**
## LangChain
The abstraction layers:
1. Layer01 - Langchain-core: **Building blocks** - Models, messages and tools; you control everything
2. Layer02 - Langgraph: **Orchestration** layer, consist of SatteGraph, nodes, edges, checkpoints; you control the flow
3. Layer03 - langchain: The **agent** loop prebuilt; you supply model, tools and prompt
4. layer04 - deepagents: **Harness** - Planning, sub agents, a filesystem; you supply intent

### Langchain-core framework
**Models**: ChatOpenAI as one interface to every LLM; invoke and stream
**Messages**: Typed message objects instead of role dicts
**Tools** The @tool decorator: docstring and type hints become the schema
**The loop** bind_tools, read .tool_calls, return ToolMessage by hand
**Structured output** Pydantic models via with_structured_output

## LangGraph
- a low-level orchestration framework and runtime for stateful, long-running agents
- Dependency graph you declare nodes that do the work and edges that say what depends on what
- Durable state survives failures; a run can resume exactly where it was interrupted

- Agent Workflows are represented as graphs
- State represents the current snapshot of the application.
- Nodes do the work.
- Edges choose what to do next.

### code carries out 5 steps
1. Define the State class
2. Start the Graph Builder
3. Create a Node
4. Create Edges
5. Compile the Graph

**note**: states are immutable
- For each field in your State, you can specify a special function called a **reducer**
- When you return a new State, LangGraph uses the **reducer** to combine this field with existing State
- his enables LangGraph to run multiple nodes concurrently and combine State without overwriting -> Example google ducs which lets multiple people change the document without overwriting others changed. google ducs chnages the stage of the states.

### Observability with LangSmith
Four lines in .env and every run is traced

1. **Set up**: sign up at smith.langchain.com, add your API key and some constants to .env per the screens (rerun load_dotenv)
2. **Every run traced**: each model call, tool call, token and latency, with no code changes
3. **Debug visually** see exactly which nodes ran, in what order, with inputs and outputs
4. **Free to start** the Developer tier includes 5k traces a month


### The Super-Step
"A super-step can be considered a single iteration over the graph nodes. Nodes that run in parallel are part of the same super-step, while nodes that run sequentially belong to separate super-steps."

One graph.invoke() call is one run: a sequence of super-steps, one per layer of nodes
 - just like one Runner.run() in the OpenAI Agents SDK

Each successive LLM call is one super-step; if it requests multiple tool calls, they run in the next super-step

Reducers merge updates within a run; the checkpointer carries State between runs


**Sep 05, 2026**
### Harness:
The surronding system that lets an AI model perform useful work reliably.

The model is the “brain”; the harness provides things such as:
- Instructions and prompts
- Tools and API access
- Conversation and state management
- Context and memory
- Permission and safety controls
- Error handling, retries, logging, and evaluation

For example, an agent harness might take a user request, send it to an LLM, execute the tool the model selects, return the result to the model, and repeat until the task is complete.

### Agent Skills
Teach an agent a capability

```
---
name: fleet-slide
description: House style for one-slide
  recommendation decks
---

# Voltway Research recommendation slide

## When to use
## House style
## Workflow
```

Frontmatter  the name and description are all the agent sees up front

Progressive disclosure  it reads the full file only when the skill is relevant

An open pattern  the same SKILL.md format Claude Code uses

**Note**: 
- The skill is really good when using the agent, but if you are building your own agent you have more flexibility to have your harness around the LLM models and control it. It is matter of if you are build or us the agent.
- Skills are lose and good for exploring what agent can do
- Tools are more robust when you need to feed your LLL models


