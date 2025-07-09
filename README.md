# ☁️ cloudmeter

**cloudmeter** is a CLI tool to measure the total data volume used across cloud data stores — both managed and unmanaged — across **AWS**, **GCP**, and **Azure**.

Whether you're optimizing storage costs, performing cloud audits, or building infra dashboards, `cloudmeter` gives you a one-command view of your multi-cloud storage footprint.

## 🚀 Features

- 🔍 Measure data usage from:
  - **AWS**: RDS, DynamoDB, S3, EBS, EFS
- 🧩 Modular architecture — easy to extend
- ✅ Works with IAM roles, service accounts, or CLI-authenticated sessions
- 🧪 Lint-safe (`ruff`), type-checked, and tested

---

## 🛠️ Installation

```bash
uv pip install --requirements pyproject.toml
```
---

## Run the CLI

Assuming that you have configured the AWS CLI with the region and right credentials and have at least `ReadOnly` access
to AWS resources, run the below command:

```bash
uv run cli.py
```

Output:
```
RDS                 0.00 GB
DYNAMODB            0.00 GB
EBS                 0.00 GB
EFS                 0.00 GB
S3                  0.00 GB
--------------------------
TOTAL               0.00 GB
```


---

## TODO

- Add support for **GCP**.
- Add support for **Azure**.
- Region-aware scanning (`--regions`)
