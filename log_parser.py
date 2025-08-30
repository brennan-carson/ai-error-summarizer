# log_parser.py

import re

def parse_error_lines(log_file_path):
    """
    Reads a log file and extracts lines containing errors or exceptions.
    Returns a list of matching log lines.
    """
    error_lines = []

    with open(log_file_path, 'r') as file:
        for line in file:
            if re.search(r'\b(ERROR|Exception)\b', line, re.IGNORECASE):
                error_lines.append(line.strip())

    return error_lines

