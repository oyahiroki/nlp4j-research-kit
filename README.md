# nlp4j-research-kit

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub](https://img.shields.io/badge/GitHub-oyahiroki%2Fnlp4j--research--kit-blue)](https://github.com/oyahiroki/nlp4j-research-kit)

A reproducible research project structure for NLP, search, and data experiments.

**Repository**: https://github.com/oyahiroki/nlp4j-research-kit

**English** | [日本語](README_ja.md)

`nlp4j-research-kit` provides a standardized directory structure and workflow for managing the entire research process:

- datasets
- preprocessing
- embeddings
- search indexes
- experiments
- metrics
- provenance
- reports

This project is designed for:

- graduate students
- NLP researchers
- search engineers
- OSS researchers
- reproducible experiment management

---

# Goals

Research projects often become difficult to manage because:

- datasets are scattered
- preprocessing scripts are lost
- experiment conditions are unclear
- metrics are not reproducible
- notebooks diverge from actual execution
- dependencies change over time

This project aims to solve these problems by providing:

- reproducible experiment structures
- standardized experiment documentation
- provenance management
- Java/Python mixed-language support
- experiment history management
- lightweight OSS-friendly workflows

---

# Features

## Reproducible Experiments

Each experiment preserves:

- configuration
- scripts
- dependencies
- runtime environment
- metrics
- generated artifacts

---

## Standardized Directory Structure

Research projects follow a unified structure.

```text
project/
├── docs/
├── data/
├── src/
├── tools/
├── configs/
├── experiments/
├── notebooks/
├── reports/
├── logs/
└── archive/
```

---

## Experiment-Centric Workflow

Each experiment is isolated and self-documented.

```text
experiments/
  exp001/
    README.md
    hypothesis.md
    config.yaml
    manifest.json

    scripts/
    tools_snapshot/

    input/
    output/
    logs/
    metrics/
    figures/
```

---

## Provenance Management

The system preserves:

- source URLs
- download timestamps
- licenses
- hashes
- runtime environments
- git commits

---

## Java + Python Mixed Environment

Supports mixed-language research environments.

```text
src/
  java/
  python/
```

---

# Recommended Workflow

## 1. Prepare Data

Place original datasets into:

```text
data/raw/
```

Example:

```text
data/raw/jawiki-20260401.xml.bz2
```

---

## 2. Preprocess Data

Generate intermediate and processed datasets.

```text
data/interim/
data/processed/
```

---

## 3. Create Experiment

Create a new experiment:

```text
experiments/exp001/
```

---

## 4. Record Hypothesis

Example:

```markdown
Wiktionary-based normalization improves embedding retrieval performance.
```

---

## 5. Run Experiment

Store:

- scripts
- configs
- metrics
- logs
- generated figures

---

## 6. Preserve Reproducibility

Save:

- requirements.txt
- pip-freeze.txt
- pom.xml
- git commit hash
- runtime versions

---

# Example Structure

```text
nlp4j-research-kit/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/
│   ├── architecture/
│   ├── papers/
│   │   ├── drafts/          # Paper drafts (Word/LaTeX)
│   │   ├── published/       # Published papers
│   │   └── reviews/         # Review comments
│   ├── presentations/       # Presentation materials (PowerPoint)
│   ├── meeting-notes/
│   └── references/
│
├── data/
│   ├── raw/
│   ├── external/
│   ├── interim/
│   ├── processed/
│   ├── embeddings/
│   ├── indexes/
│   └── metadata/
│
├── src/
│   ├── java/
│   ├── python/
│   ├── shell/
│   └── sql/
│
├── tools/
│   ├── java/
│   ├── python/
│   ├── docker/
│   └── scripts/
│
├── configs/
│   ├── datasets/
│   ├── experiments/
│   ├── models/
│   └── pipelines/
│
├── experiments/
│   ├── exp001/
│   ├── exp002/
│   └── exp003/
│
├── notebooks/
│
├── reports/
│   ├── figures/             # Figures and charts (PNG/PDF)
│   ├── tables/              # Table data (Excel/CSV)
│   ├── drafts/              # Report drafts
│   ├── submissions/         # Submission files
│   ├── presentations/       # Presentation materials
│   └── reviews/             # Review materials
│
├── logs/
│
├── tmp/
│
└── archive/
```

---

# Experiment README Example

Example:

```markdown
# exp001

## Purpose

Evaluate whether Wiktionary-based normalization improves embedding search quality.

---

## Hypothesis

Lemma normalization improves MRR.

---

## Dataset

- jawiki-20260401
- sample size: 100000

---

## Result

| metric | baseline | proposed |
|---|---:|---:|
| MRR | 0.612 | 0.644 |

---

## Observation

Normalization improved robustness against orthographic variations.

---

## Next Actions

Evaluate vocabulary filtering.
```

---

# manifest.json Example

```json
{
  "experiment_id": "exp001",
  "created_at": "2026-05-26T10:30:00+09:00",

  "git": {
    "branch": "main",
    "commit": "abc1234",
    "dirty": true
  },

  "runtime": {
    "python": "3.11.8",
    "java": "17.0.10"
  },

  "commands": [
    "python scripts/prepare_data.py",
    "java -cp app.jar nlp4j.ExperimentRunner"
  ]
}
```

---

# Design Principles

## Immutable Raw Data

Never modify:

```text
data/raw/
```

---

## Experiment = Code + Data + Hypothesis

Experiments should preserve:

- code
- datasets
- hypotheses
- metrics
- observations
- reports

---

## Preserve Failures

Failed experiments are valuable research assets.

---

## Preserve Provenance

Always preserve:

- source URLs
- licenses
- timestamps
- hashes

---

# Recommended Technologies

This template works well with:

- Python
- Java
- Jupyter Notebook
- Apache Lucene
- OpenSearch
- Elasticsearch
- MLflow
- Docker
- JSONL datasets

---

# Future Extensions

Possible future extensions:

- experiment DAG visualization
- experiment lineage tracking
- embedding visualization
- automatic README generation
- automatic paper table generation
- Lucene/OpenSearch integrations
- JSONL lineage management

---

# Quick Start

This section provides step-by-step instructions for researchers new to GitHub to get started with this project.

---

## Prerequisites

Install the following software:

1. **Git** - Version control system
   - Windows: https://git-scm.com/download/win
   - Mac: `brew install git` or https://git-scm.com/download/mac
   - Linux: `sudo apt-get install git` (Ubuntu/Debian)

2. **Python 3.8 or higher**
   - https://www.python.org/downloads/

3. **Java 11 or higher** (if using Java components)
   - https://adoptium.net/

---

## Step 1: Clone the Repository

Download (clone) the project from GitHub.

### Using Command Line

```bash
# Clone the project
git clone https://github.com/oyahiroki/nlp4j-research-kit.git

# Navigate to project directory
cd nlp4j-research-kit
```

### Using GitHub Desktop

1. Install GitHub Desktop: https://desktop.github.com/
2. File → Clone Repository
3. URL: `https://github.com/oyahiroki/nlp4j-research-kit.git`
4. Select local path
5. Click Clone

---

## Step 2: Set Up Python Environment

### Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Windows (Command Prompt)
venv\Scripts\activate.bat

# Mac/Linux
source venv/bin/activate
```

### Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

---

## Step 3: Verify Project Structure

```bash
# Check directory structure
# Windows
tree /F

# Mac/Linux
tree
```

Main directories:
- `data/` - Datasets
- `src/` - Source code
- `experiments/` - Experiments
- `docs/` - Documentation
- `reports/` - Reports and figures

---

## Step 4: Run Sample Scripts

### Run Python Sample

```bash
# Run sample script
python src/python/examples/run_sample.py
```

If you see output, it's working!

### Run Data Preparation Script

```bash
# Run data preparation script
python src/python/data/prepare_data.py
```

---

## Step 5: Create a New Experiment

### Create Experiment Directory

```bash
# Create new experiment directory
# Windows
mkdir experiments\exp002\scripts experiments\exp002\input experiments\exp002\output experiments\exp002\logs experiments\exp002\metrics experiments\exp002\figures

# Mac/Linux
mkdir -p experiments/exp002/{scripts,input,output,logs,metrics,figures}
```

### Create Experiment Documentation

```bash
# Create README.md with editor
# Windows
notepad experiments\exp002\README.md

# Mac/Linux
nano experiments/exp002/README.md
```

Copy and paste the following content:

```markdown
# exp002

## Purpose

[Describe experiment purpose]

## Hypothesis

[Describe hypothesis]

## Dataset

- Dataset name
- Sample size

## Result

| metric | baseline | proposed |
|---|---:|---:|
| - | - | - |

## Observation

[Describe observations]

## Next Actions

[Describe next actions]
```

---

## Step 6: Save Changes (Git Operations)

### Basic Git Workflow

```bash
# 1. Check changed files
git status

# 2. Stage changes (add)
git add experiments/exp002/

# 3. Commit changes (record)
git commit -m "Add exp002 experiment"

# 4. Push to GitHub (upload)
git push origin main
```

### Commonly Used Git Commands

```bash
# Check current status
git status

# View commit history
git log --oneline

# Add specific file
git add path/to/file

# Add all changes
git add .

# Commit
git commit -m "Description message"

# Pull latest from remote
git pull origin main

# Push to remote
git push origin main
```

---

## Step 7: Place Data

### Place Raw Data

```bash
# Place data in data/raw/ directory
# Example: Wikipedia dump file
cp /path/to/jawiki-20260401.xml.bz2 data/raw/
```

### Preprocess Data

```bash
# Run preprocessing script
python src/python/data/prepare_data.py
```

Processed data will be saved to:
- `data/interim/` - Intermediate data
- `data/processed/` - Final processed data

---

## Frequently Asked Questions (FAQ)

### Q1: How to verify Git installation?

```bash
git --version
```

If version is displayed, it's installed correctly.

### Q2: How to verify Python environment is set up correctly?

```bash
python --version
pip list
```

### Q3: How to verify virtual environment is activated?

Check if `(venv)` appears at the beginning of your command prompt.

```
(venv) C:\Users\username\nlp4j-research-kit>
```

### Q4: Cannot push to GitHub?

Authentication is required. Set up one of the following:

1. **Personal Access Token (Recommended)**
   - GitHub → Settings → Developer settings → Personal access tokens
   - Generate token and use it instead of password

2. **SSH Key**
   - Generate SSH key and register it on GitHub
   - Details: https://docs.github.com/en/authentication

### Q5: What to do when errors occur?

```bash
# Check detailed error messages
python -v src/python/examples/run_sample.py

# Check log files
cat logs/error.log  # Mac/Linux
type logs\error.log  # Windows
```

---

## Next Steps

1. Read the [detailed Quick Start guide](docs/QUICKSTART.md)
2. Check the [sample experiment (exp001)](experiments/exp001/)
3. Read the [Office Files Management Guide](docs/OFFICE_FILES_GUIDE.md)
4. Create your own experiments

---

## Support & Community

- **Issues**: https://github.com/oyahiroki/nlp4j-research-kit/issues
- **Discussions**: https://github.com/oyahiroki/nlp4j-research-kit/discussions
- **Wiki**: https://github.com/oyahiroki/nlp4j-research-kit/wiki

Feel free to report any questions or issues!

---

# Office Files Management

## Document Organization

### Papers and Publications

Manage paper-related files as follows:

```text
docs/papers/
├── drafts/          # Paper drafts in progress
│   ├── paper_v1.docx
│   ├── paper_v2.docx
│   └── paper_final.docx
├── published/       # Published papers
│   ├── conference_2026.pdf
│   └── journal_2026.pdf
└── reviews/         # Review comments
    ├── reviewer1_comments.docx
    └── response_to_reviewers.docx
```

### Presentations

Place presentation materials here:

```text
docs/presentations/
├── conference_2026_slides.pptx
├── lab_meeting_20260526.pptx
└── poster_session.pptx
```

### Reports and Analysis

Place experiment reports and analysis materials here:

```text
reports/
├── drafts/              # Report drafts
│   ├── monthly_report.docx
│   └── analysis_draft.docx
├── submissions/         # Submission files
│   ├── final_report.pdf
│   └── supplementary.xlsx
├── presentations/       # Presentation materials
│   └── results_presentation.pptx
├── tables/              # Table data
│   ├── experiment_results.xlsx
│   ├── metrics_comparison.xlsx
│   └── statistics.csv
└── figures/             # Figures and charts
    ├── figure1.png
    └── chart1.pdf
```

---

## File Naming Conventions

### Papers

```text
[type]_[venue]_[year]_[version].docx
Example: paper_icml_2026_v3.docx
```

### Presentations

```text
[event]_[date]_[topic].pptx
Example: lab_meeting_20260526_results.pptx
```

### Reports

```text
[type]_[period]_[version].docx
Example: monthly_report_202605_final.docx
```

### Tables

```text
[content]_[experiment]_[date].xlsx
Example: metrics_exp001_20260526.xlsx
```

---

## Version Control Strategy

### For Text Documents (Word/PowerPoint)

1. **Major versions**: Use version numbers in filename
   - `paper_v1.docx`, `paper_v2.docx`, `paper_v3.docx`

2. **Final versions**: Mark with `_final` suffix
   - `paper_final.docx`, `report_final.docx`

3. **Dated versions**: Use ISO date format
   - `slides_20260526.pptx`

### For Data Files (Excel)

1. **Keep raw data separate**: Store in `data/raw/`
2. **Processed tables**: Store in `reports/tables/`
3. **Use CSV for version control**: Convert to CSV when possible

---

## Best Practices

### Word Documents

- Use styles for consistent formatting
- Enable track changes for collaborative editing
- Export final versions to PDF
- Keep backup copies in `archive/`

### Excel Files

- Use named ranges for important data
- Document formulas and calculations
- Export key tables to CSV for version control
- Keep one sheet per logical table

### PowerPoint Files

- Use master slides for consistency
- Export figures as high-resolution images
- Save presenter notes separately
- Archive old versions regularly

---

## Integration with Experiments

Managing Office files per experiment:

```text
experiments/exp001/
├── README.md
├── figures/
│   ├── result_chart.xlsx    # Data for creating figures
│   └── result_chart.png     # Generated figure
├── metrics/
│   └── metrics_summary.xlsx # Metrics summary
└── reports/
    └── experiment_report.docx  # Experiment report
```

---

# Philosophy

Research should be:

- reproducible
- traceable
- explainable
- organized
- shareable

This project aims to make research projects easier to maintain over long periods of time.

---

# License

Apache License 2.0
````
