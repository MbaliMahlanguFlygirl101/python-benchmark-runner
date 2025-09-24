#!/usr/bin/env python3

import os
import subprocess
import sys
import time

def run_benchmark(script_path):
    print(f"\nRunning benchmark: {script_path}")
    start = time.perf_counter()
    try:
        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True, check=True)
        output = result.stdout
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")
        print(e.output)
        return
    end = time.perf_counter()
    print(f"Execution time for {script_path}: {end - start:.4f} seconds")

def main(directory):
    py_files = [f for f in os.listdir(directory) if f.endswith('.py') and f != os.path.basename(__file__)]
    if not py_files:
        print("No Python scripts found for benchmarking.")
        return
    for script in py_files:
        run_benchmark(os.path.join(directory, script))

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    main(directory)