from dataclasses import dataclass


@dataclass
class UsageRecord:
    provider: str  # 'aws'
    service: str  # 'rds', 'ebs', etc.
    size_mb: float


def mb_to_gb(mb: float) -> float:
    return round(mb / 1024, 2)
