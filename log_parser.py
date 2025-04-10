# log_parser.py
# Author: Cyborg Knight
# Simple log parser that flags suspicious entries based on keywords

import sys

# Define suspicious keywords to look for
suspicious_keywords = [
    "error", "failed", "unauthorized", "denied", "invalid", "attack",
    "exploit", "refused", "brute", "malware", "injection"
]

def parse_log(file_path):
    try:
        with open(file_path, 'r') as logfile:
            print(f"\n🔍 Scanning {file_path} for suspicious entries...\n")
            line_count = 0
            hit_count = 0

            for line in logfile:
                line_count += 1
                for keyword in suspicious_keywords:
                    if keyword in line.lower():
                        print(f"[!] Line {line_count}: {line.strip()}")
                        hit_count += 1
                        break

            print(f"\n✅ Done. Scanned {line_count} lines. Found {hit_count} suspicious entries.\n")

    except FileNotFoundError:
        print(f"[X] File not found: {file_path}")
    except Exception as e:
        print(f"[X] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_parser.py <logfile>")
    else:
        parse_log(sys.argv[1])
