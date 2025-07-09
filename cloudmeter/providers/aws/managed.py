import boto3

from cloudmeter.core import UsageRecord

def rds() -> UsageRecord:
    client = boto3.client("rds")
    size_gb = sum(db.get("AllocatedStorage", 0) for db in client.describe_db_instances()["DBInstances"])
    return UsageRecord("aws", "rds", size_gb * 1024)

def dynamodb() -> UsageRecord:
    client = boto3.client("dynamodb")
    total_bytes = 0
    for table in client.list_tables()["TableNames"]:
        desc = client.describe_table(TableName=table)
        total_bytes += desc["Table"].get("TableSizeBytes", 0)
    return UsageRecord("aws", "dynamodb", total_bytes / (1024 * 1024))

# def documentdb() -> UsageRecord:
#     # client = boto3.client("docdb")
#     # API does not expose size directly, this is a placeholder
#     # cluster_count = len(client.describe_db_clusters()["DBClusters"])
#     return UsageRecord("aws", "documentdb", 0)
