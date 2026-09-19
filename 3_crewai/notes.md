# Week 3 Summary
**Resource**: 
- https://github.com/ed-donner/agents
- https://drive.google.com/drive/folders/1v0wMtpitoDI0vIqP3556J5Pl73oFnOPD
- https://serper.dev/


**SEP 02,2026**
## Main Concepts in CrewAI
**Agents**: an autonomus unit, with and LLM, a role, a goal, a backstory, memory, tools

**Note**: Because it is opinionated framwork it has less transparancy, but it is really good at writing prompt systems

**Tasks**: a specific assignment to be carries out, with a description, expected output, agent

**Crew**: a team of Agents and Tasks; either: Sequential run tasks in order they are defined historical use a Manger LLM  to assign

- Lightweight, but somewhat more opinionated than OpenAI Agents SDK - more terminology, marginally more prescriptive
- ..and with an ability to get much more prescriptive
- What CrewAI is eally good is to be clear in the architecture to build

Subtle gotchas:
Google key must be GEMINI_API_KEY
Sometimes crewai creates a new .env file that can override course .env file. If so, delete the new one.
CrewAI calls load_dotenv() not load_dotenv(override=True) and that means system level env variables take priority

**Sep 03, 2026**
### Some useful commands for running crewai
- crewai traces enable
- crewai run
- crewai create crew my_project
- uv python pin 3.13 -> if you need to change your python version

### Five steps of crewai project
1. Create the project with: crewai create crew my_project
2. Fill in the config yaml files to define the Agents and Tasks
3. Complete the crew.py module to create the Agents, Tasks and Crew, referencing the config
4. Update main.py to set any inputs
5. Run with: crewai run

**Note**: Static info should go through Yaml file

- context (in yaml file example fianantial_resaercher (tasks)):  # this is for letting the agent what should be included in the analysis task as a context form other tasks. To make sure if the context is includesd in the task.
- Crew by default incudes all the context from prior tasks. We use context field to control it for each task.
- three ways of setting up the tracing:
    - Either set tracing=True in the Crew() constructor
    - or CREWAI_TRACING_ENABLED=true env variable
     - or crewai tracing enable


