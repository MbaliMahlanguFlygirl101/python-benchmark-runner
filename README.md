# python-benchmark-runner
A Python tool to run, time, and parse results from multiple benchmark scripts in a directory. Automatically discovers `.py` files, executes each, captures `RESULT: key=value` lines, and prints a summary of benchmark results and execution times.
# Python Benchmark Runner

A simple Python tool to automate running, timing, and parsing results from multiple Python benchmark scripts in a directory.

This script will:
- Discover all `.py` files in a specified directory.
- Execute each script, measure its execution time, and capture its output.
- Parse benchmark result lines (e.g., `RESULT: timing=0.123`) from each script’s output.
- Print a summary of all benchmark results and execution times.

Perfect for testing and comparing performance of different Python implementations or algorithms!

## Usage

```bash
python3 run_and_parse_benchmarks.py [directory]
```
- If no directory is given, the current folder is used.

Make sure your benchmark scripts print result lines in the format:
```
RESULT: key=value
```

## Example

```
RESULT: timing=0.123
RESULT: accuracy=0.98
```

## License

MIT
