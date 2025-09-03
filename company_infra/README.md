# Company Infra

This directory contains infrastructure configuration for the Brisingr project
using [Sky Serve](https://sky.cs.berkeley.edu/).

## Layout

```
company_infra/
├─ docker/
│  └─ llm.Dockerfile
├─ env/
│  ├─ base-requirements.txt
│  ├─ llm-requirements.txt
│  └─ vision-requirements.txt
├─ sky/
│  ├─ base-cluster.yaml
│  ├─ llm-workload.yaml
│  └─ vision-workload.yaml
└─ scripts/
   └─ launch_workload.py
```

## Usage

1. **Launch cluster**
   ```bash
   sky launch -c company_infra/sky/base-cluster.yaml
   ```
2. **Serve an LLM**
   ```bash
   sky serve up -c company_infra/sky/llm-workload.yaml
   ```
3. **Serve a vision model (example)**
   ```bash
   sky serve up -c company_infra/sky/vision-workload.yaml
   ```

Adjust dependency versions and model paths in the requirements files and
scripts as needed.
