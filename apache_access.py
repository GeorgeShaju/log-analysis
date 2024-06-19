import re
from collections import Counter

def analyze_log(log_file):
    log_pattern = r'^(\S+) (\S+) (\S+) \[([^\]]+)\] "(\S+) (\S+) (\S+)" (\d+) (\d+)'
    total_requests = 0
    error_404_count = 0
    page_requests = Counter()
    ip_requests = Counter()

    try:
        with open(log_file, 'r') as file:
            for line in file:
                match = re.match(log_pattern, line)
                if match:
                    total_requests += 1
                    status_code = int(match.group(8))
                    request_method = match.group(5)
                    requested_page = match.group(6)
                    client_ip = match.group(1)

                    if status_code == 404:
                        error_404_count += 1
                    if request_method == "GET" or request_method == "POST":
                        page_requests[requested_page] += 1
                    ip_requests[client_ip] += 1

    except FileNotFoundError:
        print(f"Error: The file '{log_file}' was not found.")
        return

    print("----- Log Analysis Report -----")
    print(f"Total Requests: {total_requests}")
    print(f"404 Errors: {error_404_count}")
    print("\nMost Requested Pages:")
    for page, count in page_requests.most_common(5):
        print(f"{page}: {count} requests")
    print("\nIP Addresses with Most Requests:")
    for ip, count in ip_requests.most_common(5):
        print(f"{ip}: {count} requests")
if __name__ == "__main__":
    log_file = "apache.log"
    analyze_log(log_file)
