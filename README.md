<<<<<<< HEAD
# AI Engineering: 60-Day Learning Journey

A hands-on learning repository for building practical AI engineering skills over
60 days. The goal is to progress from calling language model APIs to designing,
testing, and delivering useful AI applications.

## Learning goals

- Build a strong foundation in Python and language model APIs.
- Practice prompt design, structured outputs, and reliable application code.
- Learn retrieval-augmented generation (RAG), evaluation, and deployment basics.
- Keep experiments, notes, and project work organized and reproducible.

## Roadmap

The plan is grouped into nine weeks. Weeks 1–8 cover seven days each, and Week 9
covers the final four days, for a total of 60 days. Topics after the current
starter materials are a roadmap, not a claim that the work is already complete.

| Week | Focus |
| --- | --- |
| Week 1 | Python setup, LLM APIs, prompts, and first experiments |
| Week 2 | Prompt engineering, chat workflows, and structured responses |
| Week 3 | Embeddings, vector search, and semantic retrieval |
| Week 4 | Retrieval-augmented generation (RAG) applications |
| Week 5 | Tool calling, agents, and workflow orchestration |
| Week 6 | Evaluation, testing, and improving AI application quality |
| Week 7 | Data preparation, safety, and responsible AI practices |
| Week 8 | Deployment, monitoring, and production-minded engineering |
| Week 9 | Capstone polish, documentation, and learning review (Days 57–60) |

## Repository structure

```text
Week-1/
  Day-1/
  Day-2/
requirements.txt
README.md
```

Existing day folders and files are being preserved in place. Add later work as
`Week-2/Day-8/` onward, following the same `Week-N/Day-N/` pattern. No files
have been moved as part of this setup.

## Current progress

- Week 1: starter materials are present for Day 1 and Day 2.
- Current examples call the Groq chat completions API and load the API key from
  an environment file.
- Update this section as each day's work is completed; files being present does
  not necessarily mean the lesson has been completed.

## Technologies

- Python 3.14 or newer, as declared by the existing day projects.
- Groq Python SDK for chat completions.
- `python-dotenv` for loading local environment variables.
- `uv` is used by the existing day folders to manage Python projects.

## Setup

From the repository root, create and activate a virtual environment, then
install the shared dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Create a local `.env` file in the directory from which you run a script and add
your own key:

```text
GROQ_API_KEY=your_groq_api_key
```

Never commit `.env` files, API keys, or other credentials. The `.gitignore`
rules exclude them from Git. If a key has ever been published, revoke it with
the provider and replace it.

Run an existing example from its own folder:

```powershell
Set-Location .\Week-1\Day-1
python .\Hello_LLM.py
```

```powershell
Set-Location .\Week-1\Day-2
python .\sys_temp.py
```

## Projects

The current starter projects are small Groq-powered chat experiments: a basic
chat completion and a system-prompt-based brand-name generator. A suitable
capstone direction for the later weeks is a documented, evaluated RAG
application; its scope can evolve as the learning plan progresses.

## Progress tracking

Add brief notes to each day's README covering the concept studied, what was
built, and what remains to try. Keep API credentials, private data, virtual
environments, and generated caches out of the repository.
=======
# ai-engineering-60-days
>>>>>>> 63ec87b6ed9687e3fefcd81625e53ecdf2816b1e
