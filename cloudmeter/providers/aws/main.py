from cloudmeter.providers.aws import managed, unmanaged

SERVICES = [
    managed.rds,
    managed.dynamodb,
    managed.documentdb,
    unmanaged.ebs,
    unmanaged.efs,
    unmanaged.s3,
]
