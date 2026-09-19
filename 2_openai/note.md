# Week 2 Summary
**Resource**: 
- https://github.com/ed-donner/agents
- https://drive.google.com/drive/folders/1JHXOClW73oUSnbIffdIn64QMfAa227eN
- https://openai.github.io/openai-agents-python/multi_agent/
- https://openai.github.io/openai-agents-python/guardrails/
- https://openai.github.io/openai-agents-python/sandbox_agents/
- https://openai.github.io/openai-agents-python/tools/#hosted-tools

**Aug 30,2026**
## Asyncio
- It is used for parallel process 
- Asyncio is the light wiighted the multi-processing
- In Sync you define how the functions are interact with each other

Asyncio provides a lightweight alternative to threading or multiprocessing

Functions defined with async def are called coroutines — they’re special functions
that can be paused and resumed

Calling a coroutine doesn’t execute it immediately — it returns a coroutine object

To actually run a coroutine, you must await it, which schedules it for execution
within an event loop

While a coroutine is waiting (e.g. for I/O), the event loop can run other coroutines

### Three Main Component of Async

1. async def fn
2. await fn
3. await asyncio.gather(fn1 , fn2, etc)

### When you are using the Asynco
1. When we are working with LLMs, because they are typically in I/O bands, you are waiting the stuff commmin out of netework. In those scenarios Async is ideal, because it is waiting to chopping your coroutine
2. Not ideal for heaviliy cpu bound, lots of calculations, because asynco is useless because it does every code at a time and you need to look at multi-threading, multi-processing.

**Note** threasds are the thinngs come from operating system overheads as processes, but asynco is not. It is just a loop which compete for the events come early.

We have many bounds two examples:
- I/O Bound
- compute Bound

### Initial Terminalogy
- **Agents** represent a particular LLM with system prompt and tools
- For collaboration: **Agents as tools** and **Handsoffs** for collaboration
- **Gardrails** represent controls

### Three steps for building the Agents
1. Create an ubstance of Agent
2. Use **with trace()** to track the agent
3. Call Runner.run() to run one "Application Level Turn" the runner keeps looping until it reaches a stopping points.

### With Coding Agents: Be the Boss
- Invest in your prompts: Be precise, ensure current APIs, Demand conciseness - no slop!
- Start SIMPLE
- Work incrementally; test constantly; validate success criteria
- Don’t get lazy - challenge & demand evidence
- Handle frustration with style

Above all: your objective is to learn; it’s great to use Coding Agents to help, but there’s no point in letting them build everything
