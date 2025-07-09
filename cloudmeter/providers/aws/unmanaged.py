import boto3

from cloudmeter.core import UsageRecord


def ebs() -> UsageRecord:
    client = boto3.client("ec2")
    size_gb = sum(vol["Size"] for vol in client.describe_volumes()["Volumes"])
    return UsageRecord("aws", "ebs", size_gb * 1024)


def efs() -> UsageRecord:
    client = boto3.client("efs")
    total_bytes = sum(
        fs["SizeInBytes"]["Value"]
        for fs in client.describe_file_systems()["FileSystems"]
    )
    return UsageRecord("aws", "efs", total_bytes / (1024 * 1024))


def s3() -> UsageRecord:
    client = boto3.client("s3")
    total_bytes = 0
    for bucket in client.list_buckets()["Buckets"]:
        paginator = client.get_paginator("list_objects_v2")
        try:
            for page in paginator.paginate(Bucket=bucket["Name"]):
                total_bytes += sum(obj["Size"] for obj in page.get("Contents", []))
        except Exception:
            continue
    return UsageRecord("aws", "s3", total_bytes / (1024 * 1024))
