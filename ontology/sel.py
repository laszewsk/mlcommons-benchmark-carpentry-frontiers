#!/usr/bin/env python3
"""
Filter LaTeX longtable columns.

Usage:
  filter_table.py --in=INFILE --out=OUTFILE --columns=COLUMNS
  filter_table.py [--in=INFILE] [--out=OUTFILE] [--columns=COLUMNS]

Options:
  --in=INFILE        Input LaTeX file. [default: table.tex]
  --out=OUTFILE      Output LaTeX file. [default: output.tex]
  --columns=COLUMNS  Comma-separated list of column names. [default: Ratings,Name,Domain,Models,Metrics,Citation]

Example:
  filter_table.py --in=table.tex --out=filtered.tex --columns="Name,Domain,Models"
"""

from docopt import docopt
import re

def extract_column_headers(header_line):
    """Extract column names from a LaTeX header line containing \textbf{}."""
    parts = header_line.split("&")
    headers = []
    for p in parts:
        m = re.search(r'\\textbf\{([^}]+)\}', p)
        if m:
            headers.append(m.group(1).strip())
    return headers

def filter_table(lines, keep_columns):
    """Return new table lines keeping only the requested columns."""
    new_lines = []
    header_found = False
    selected_indices = []

    for line in lines:
        if not header_found and "\\textbf{" in line and "&" in line:
            # Extract headers
            headers = extract_column_headers(line)
            header_found = True

            # Map selected column names to indices
            selected_indices = [headers.index(c) for c in keep_columns if c in headers]

            # Build filtered header line
            filtered_header = " & ".join(
                [f"\\textbf{{{headers[i]}}}" for i in selected_indices]
            ) + " \\\\ \\hline\n"
            new_lines.append(filtered_header)
            continue

        if header_found and "&" in line and "\\\\" in line:
            # Table row
            parts = [p.strip() for p in line.split("&")]
            filtered_parts = [parts[i] for i in selected_indices if i < len(parts)]
            new_lines.append(" & ".join(filtered_parts) + " \\\\ \\hline\n")
        else:
            # Non-row lines: copy as-is
            new_lines.append(line)

    return new_lines


def main():
    args = docopt(__doc__)

    infile = args["--in"]
    outfile = args["--out"]
    keep_columns = [c.strip() for c in args["--columns"].split(",")]

    with open(infile, "r") as f:
        lines = f.readlines()

    filtered = filter_table(lines, keep_columns)

    with open(outfile, "w") as f:
        f.writelines(filtered)

    print(f"✔ Wrote filtered table to {outfile}")
    print(f"✔ Columns kept: {', '.join(keep_columns)}")


if __name__ == "__main__":
    main()
