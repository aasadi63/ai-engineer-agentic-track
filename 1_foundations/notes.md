# Lab 2
**Resource**: 
- https://github.com/ed-donner/agents
- https://drive.google.com/drive/folders/1ObUv9QvP6MgdvY73iUG1GWQPkCDsfzVW
- https://pushover.net/
**Aug 26, 2026**
## Definition of an AI Agent
**Sam Altman** definition
- AI systems that can do work for you independently

**Anthropic, Hugging Face, ...** in early 2025 concensus
- AI systems where an LLM controls the workflow

**Currrent prevailing veiw**
- An LLM with Tools in a Loop to achieve a goal

## Agentic Systems
### Anthropic distingush two types
1. **Workflows**: are systems where LLMs and tools are orchestrated through predefined code path
2. **Agents** are dynamic systems where LLMs direct their own processes and tool usage, maintiainng control over how they accomplish tasks

### Anthropic 5 workflow design patterns ([resource](https://www.anthropic.com/engineering/building-effective-agents))
1. Prompt Chaining: Decompose into fixed sub-tasks
2. Routing: Direct an input into specialized sub-task, ensuring separation of concerns
3. Parallelization: Breaking down tasks and running multiple subtask concurrent
4. Orchestrator-worker: Complex tasks are broken down dynamically and combined
5. Evaluator-Optimizer: LLM output is validated by another

**By contrast, Agents**:
1. Open-ended
2. Feedback loops
3. No fixed path

## Risk of Agent Frameworks
- Unpredictable path
- Unpredictable output
- Unpredictable cost
- Monitor (Observability, Evals)
- "Guardrails ensure your agents behave safely, consistently, and within your intended boundaries"

### The First Agent Trap
- I need an Agent for my businees
    - "OK- and what businees problem is that solving?"
- I want an Strategy Agent to give me advice for my org
    - OK, right, and.. what.. business problem is that solving

**Note**: LLM are really good at generating the content, but it is important to know how to fit and messure in our business context

### The Second Agent Trap Anthropomorphizing
- A common red flag: "Agent Architectures" that assign human-like responsibilities to agents
- The right approach: Start simple, and measure performance againist a business objective and Agents becasue it improves performance

**Takeaways**:
- Build Agent systems to solve problems in a measurable way
- Decide your Agent Architecture based on performance
- LLMs generate pausible output, not necessarily accurate outputs.
- Aligning the outputs with business results? That's your job.

### Confusing Teminalogy
**What is an Agentic Engineer**?
- someone who uses Agents to Engineer or Someone who engineers Agents

### Providers:
1. OpenAI: GPT nano, GPT mini, GPT
2. Anthropic: Claude Haiku, Claude Sonnet, Claude Opus
3. Google: Gemini Flash Lite, Gemini Flash, Gemini Pro
4. DeepSeek AI: DeepSeek V4
5. Groq: open-source LLMs 
6. Ollama: local open-source
- Artificial Analysis gives a comparison of the intelligence, speed and cost of models at https://artificalanalysis.ai

**Aug 28, 2026**
### The Agent Landscape
Different types of offering related ti AI agents:
- Builders: Non technical people can build AI Agents. Example n8n, ElevenLabs, OpenAI Agent Builder, CrewAI Studio -> AI Builder
- Products: Non technical people can use AI Agents. Example like Claude Code, Cowork, OpenClaw, Claude Design -> AI Coder
- Runtime: Technical people can execute AI Agents. AWSLambda, AWS Bedrock AgentCore, Claude Manged Agents, Vertex AI Agent Engine -> AI Engineer Production Track
- Frameworks: Technical people can **develop** AI Agents: OpenAI Agents SDK, CrewAI, LangGraph/ LngChain, Google SDK -> AI Engineer, Agentic Track

### Agent Frameworks
Helper code that makes it easier to create Agents based on LLM calls. They are covering:
- Orchestration - chaining together LLM calls
- Tool calling - equipping an LLM with abilitties, including with MCP
- Constructing LLM inputs and interpreting outputs - including a technique called ‘Structured Outputs’

This allows you to easily code an ‘Agent Loop’ - an LLM in a loop with tools to achieve a goal

### Agent Frameworks
- Start with lightweight framework: OpenAI Agents SKD, Google SKD, AWS Strands Agents
- Opinionated framework: CrewAI, LangGraph / LangChain
- No Framework -> we start here

### Tools
gives LLMs abilities. The power to carry out actions like query a database or look up stock prices.

**Note**: 
- Agentic AI involves building a harness around LLMs, crafting the inputs and interpreting the outputs, in a loop, so that they can ‘use tools’ and ‘be autonomous’
- Agent Frameworks are helper code that make it faster to implement these techniques, but they’re not required
- By the end of this course, you will be able to deliver significant commercial value by building 
- autonomous AI Agents

### Context Engineering
Resource: https://www.philschmid.de/context-engineering

Agentic RAG: providing tool for Agent to retrieve useful information
Short Term Memory: 
Long term meomory: the information that related to prior converstion or stored other place through RAG
 


