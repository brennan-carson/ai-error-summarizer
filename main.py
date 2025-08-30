# main.py

from log_parser import parse_error_lines
from summarizer import generate_summary

def main():
    log_file = "sample.log"
    
    print(f"Reading logs from: {log_file}")
    errors = parse_error_lines(log_file)

    print(f"Found {len(errors)} error lines.")
    if errors:
        summary = generate_summary(errors)
        print("\n--- Summary Report ---\n")
        print(summary)
    else:
        print("No error lines found in log.")

if __name__ == "__main__":
    main()

