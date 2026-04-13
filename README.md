# Engineering Team (CrewAI)

Multi-agent **software delivery** crew: one module of Python backend, a **UX/UI specification**, a **Gradio** demo, and **QA** (written plan plus **pytest** automation). Built with [CrewAI](https://crewai.com).

## What it builds (default brief)

Kickoff inputs in `src/engineering_team/main.py` drive the run:

- **Domain:** perishable inventory for a small food retail / meal-prep scenario (batches, expiry, receive / sell / waste, FIFO-style allocation policy, pricing stub `get_retail_price(sku)`, reporting and audit ledger).
- **Backend:** single file `inventory.py`, main class `Inventory`.
- **Outputs:** see [Artifacts](#artifacts) below.

To change the product, edit the `requirements` string plus `module_name` and `class_name` in `main.py`.

## Architecture

**Process:** sequential crew (`Process.sequential` in `crew.py`).

**Agents** (`config/agents.yaml`):

| Agent | Role |
|--------|------|
| **engineering_lead** | Backend design: one self-contained module, APIs and structure in markdown. |
| **ux_ui_engineer** | UX/UI spec for the Gradio demo (flows, layout, copy, states, light accessibility). |
| **backend_engineer** | Implements the design in `{module_name}`; optional **safe code execution** (Docker). |
| **frontend_engineer** | Implements `app.py` using the **UX/UI spec** and the real backend API. |
| **test_engineer** | QA owner: **test/quality plan** (markdown), then **pytest** module `test_{module_name}`. |

**Task pipeline** (`config/tasks.yaml`):

1. `design_task` → engineering lead → `output/{module_name}_design.md`
2. `ux_ui_task` → UX/UI → `output/ux_ui_spec.md`
3. `code_task` → backend → `output/{module_name}` (e.g. `output/inventory.py`)
4. `frontend_task` → Gradio → `output/app.py`
5. `qa_planning_task` → QA plan → `output/qa_test_plan.md`
6. `test_task` → pytest → `output/test_{module_name}` (e.g. `output/test_inventory.py`)

Wiring and execution settings (verbose mode, code execution flags) live in `src/engineering_team/crew.py`.

## Artifacts

All generated files are written under **`output/`** (the directory is created at runtime from `main.py`). Paths use the `module_name` placeholder from kickoff (e.g. `inventory.py` → design file name includes `.py` in the stem).

## Prerequisites

- **Python** >=3.10, < 3.13
- **API keys** in **`.env`** at the project root of this package (`3_crew/engineering_team/.env`), or as required by your CrewAI / provider setup. Agents use multiple providers (e.g. OpenAI and Anthropic) depending on `agents.yaml`; configure keys for whichever models you reference.
- **Docker** (recommended): backend and test agents use `code_execution_mode="safe"` in `crew.py`, which relies on Docker for isolated execution.

## Installation

This project uses [uv](https://docs.astral.sh/uv/) and CrewAI conventions.

```bash
cd 3_crew/engineering_team
pip install uv   # if needed
crewai install   # or: uv sync, per your workflow
```

## Running

From **`3_crew/engineering_team`** (where `pyproject.toml` lives):

```bash
crewai run
```

This loads `EngineeringTeam`, substitutes `requirements`, `module_name`, and `class_name` from `main.py`, and runs the full task chain.

## Customization

| File | Purpose |
|------|---------|
| `src/engineering_team/main.py` | Product brief (`requirements`), `module_name`, `class_name`. |
| `src/engineering_team/config/agents.yaml` | Roles, goals, LLM ids per agent. |
| `src/engineering_team/config/tasks.yaml` | Task text, context edges, `output_file` paths. |
| `src/engineering_team/crew.py` | Agents, tasks, `Crew` settings (sequential process, code execution). |

Optional tools can be added in `src/engineering_team/tools/` and attached in `crew.py` (the included `custom_tool.py` is a stub and is not wired by default).

## Pushing to your own GitHub repo

This folder may live inside a larger monorepo. To publish **your fork or your copy** under **your** GitHub account:

1. Create a **new empty repository** on GitHub (no need to add a README if you already have this tree).
2. From the **git root** that contains the commits you want (e.g. the parent `agents` repo, or a repo that only contains `engineering_team`), set the remote to your repo:

   ```bash
   git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   ```

   Or keep the course/upstream remote and add yours:

   ```bash
   git remote rename origin upstream
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```

3. **Never commit `.env`**; it should stay gitignored. Rotate any key that was ever committed.

## CrewAI resources

- [CrewAI documentation](https://docs.crewai.com)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewai)
