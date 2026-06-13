```python
import subprocess
import sys
from pathlib import Path


PIPELINE_STEPS = [
    {
        "name": "Bronze Layer: Load and profile raw MLS-style exports",
        "script": Path("scripts/bronze/01_load_raw_mls_exports.py"),
    },
    {
        "name": "Silver Layer: Clean and standardize lead records",
        "script": Path("scripts/silver/02_clean_and_standardize_leads.py"),
    },
    {
        "name": "Gold Layer: Build campaign-ready outreach queue",
        "script": Path("scripts/gold/03_build_campaign_queue.py"),
    },
    {
        "name": "Analytics Layer: Generate campaign summary",
        "script": Path("scripts/analytics/04_generate_campaign_summary.py"),
    },
]


def run_step(step):
    """Run one pipeline step and stop if it fails."""
    script_path = step["script"]

    if not script_path.exists():
        raise FileNotFoundError(f"Missing pipeline script: {script_path}")

    print("\n" + "=" * 80)
    print(f"Running: {step['name']}")
    print(f"Script: {script_path}")
    print("=" * 80)

    subprocess.run([sys.executable, str(script_path)], check=True)


def main():
    print("\nLuxury Rental Lead Pipeline & MLS Outreach Automation System")
    print("Starting public-safe synthetic data pipeline...")

    for step in PIPELINE_STEPS:
        run_step(step)

    print("\n" + "=" * 80)
    print("Pipeline completed successfully.")
    print("=" * 80)

    print("\nGenerated outputs:")
    print("datasets/analytics/raw_data_profile_mock.csv")
    print("datasets/cleaned/cleaned_luxury_listing_leads.csv")
    print("outputs/campaign_queue_mock.csv")
    print("datasets/analytics/campaign_summary_mock.csv")


if __name__ == "__main__":
    main()
```
