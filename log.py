# Function to read and analyze a log file
def analyze_log_file(log_file):
    # Initialize counters for each log level
    info_count = 0
    error_count = 0
    warning_count = 0

    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if "[INFO]" in line:
                    info_count += 1
                elif "[ERROR]" in line:
                    error_count += 1
                elif "[WARNING]" in line:
                    warning_count += 1
    
    except FileNotFoundError:
        print(f"Error: The file '{log_file}' was not found.")
        return

    # Print analysis results
    print("Log file analysis results:")
    print(f"INFO: {info_count} occurrences")
    print(f"ERROR: {error_count} occurrences")
    print(f"WARNING: {warning_count} occurrences")

# Example usage:
if __name__ == "__main__":
    log_file = "example.log"
    analyze_log_file(log_file)
