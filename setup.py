import os

base = "data-lake-gcp-project"

folders = [
    f"{base}/scripts",
    f"{base}/architecture",
    f"{base}/data/bronze",
    f"{base}/data/silver",
    f"{base}/data/gold",
    f"{base}/src/data_ingestion",
    f"{base}/src/data_processing",
    f"{base}/src/cloud_functions",
    f"{base}/docs",
    f"{base}/queries",
    f"{base}/dashboard",
]

files = [
    f"{base}/README.md",
    f"{base}/requirements.txt",

    f"{base}/scripts/gcp_setup.sh",
    f"{base}/scripts/upload_data.sh",
    f"{base}/scripts/lifecycle_policy.json",

    f"{base}/architecture/data_flow_diagram.png",
    f"{base}/architecture/architecture_notes.md",

    f"{base}/src/data_ingestion/upload_to_gcs.py",
    f"{base}/src/data_processing/validate_schema.py",
    f"{base}/src/data_processing/transform_data.py",
    f"{base}/src/cloud_functions/move_bronze_to_silver.py",

    f"{base}/docs/iam_roles.md",
    f"{base}/docs/data_retention.md",
    f"{base}/docs/schema_strategy.md",
    f"{base}/docs/cost_estimation.md",

    f"{base}/queries/bigquery_queries.sql",

    f"{base}/dashboard/looker_dashboard_link.txt",
]


for folder in folders:
    os.makedirs(folder, exist_ok = True)

for file in files:
    open(file , "w").close()

print("Project structure created!")