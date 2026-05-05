#!/usr/bin/env python3

import argparse


def build_report(target: str, competitors: list[str], lenses: list[str]) -> str:
    coverage_rows = "\n".join(
        f"| {competitor} |  |  |  |" for competitor in competitors
    )
    comparison_rows = "\n".join(
        f"| {competitor} |  |  |  |  |  |  |" for competitor in competitors
    )
    lens_text = ", ".join(lenses)
    return f"""# Competitor Analysis Report

## Focal Target

- Focal target: {target}
- Category:
- Scope:
- Matching note:

## Competitor Set

{chr(10).join(f"- Competitor: {competitor}{chr(10)}  Inclusion logic:" for competitor in competitors)}

## Coverage Summary

| Competitor | Sources used | Evidence quality | Notes |
| --- | --- | --- | --- |
{coverage_rows}

## Comparison Table

| Competitor | Role | Price | Focal offer | Main claims | Trust proof | Gap |
| --- | --- | --- | --- | --- | --- | --- |
{comparison_rows}

## Key Differences

### 1. Difference

- Why it matters:
- Confidence:
- Seen in:

Example pages:
- 

## Commercial Judgments

- Judgment:
  Basis:
  Why it matters:

## Confidence And Gaps

- Lenses used: {lens_text}
- 

## Suggested Next Move

- 
"""


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render a markdown starter report for public competitor analysis."
    )
    parser.add_argument("--target", required=True, help="Target product or brand name")
    parser.add_argument(
        "--competitors",
        nargs="+",
        required=True,
        help="Competitors to include in the report",
    )
    parser.add_argument(
        "--lenses",
        nargs="+",
        default=["positioning", "pricing", "claims", "reviews"],
        help="Comparison lenses to record in the report",
    )
    args = parser.parse_args()
    print(build_report(args.target, args.competitors, args.lenses))


if __name__ == "__main__":
    main()
