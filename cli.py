import typer

from cloudmeter.providers.aws import main as aws
from cloudmeter.core import mb_to_gb

app = typer.Typer()

@app.command()
def aws_summary():
    """Summarize AWS data store usage"""
    total_mb = 0
    for collector in aws.SERVICES:
        usage = collector()
        print(f"{usage.service.upper():<12}  {mb_to_gb(usage.size_mb):>10.2f} GB")
        total_mb += usage.size_mb
    print("-" * 26)
    print(f"{'TOTAL':<12}  {mb_to_gb(total_mb):>10.2f} GB")

if __name__ == "__main__":
    app()
