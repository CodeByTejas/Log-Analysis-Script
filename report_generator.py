"""Module for generating analysis reports."""
import csv
from typing import List, Tuple

def format_table(data: List[Tuple[str, int]], headers: List[str]) -> str:
    """Format data into a simple ASCII table."""
    if not data:
        return "No data available"
    
    # Here we are converting all values to strings and find max widths
    str_data = [[str(cell) for cell in row] for row in [headers] + list(map(list, data))]
    widths = [max(len(row[i]) for row in str_data) for i in range(len(headers))]
    
    # Creating the table
    lines = []
    
    # Header
    header = " | ".join(f"{h:<{w}}" for h, w in zip(headers, widths))
    lines.append(header)
    
    # Separators
    separator = "-+-".join("-" * w for w in widths)
    lines.append(separator)
    
    # Data rows
    for row in data:
        str_row = " | ".join(f"{str(cell):<{w}}" for cell, w in zip(row, widths))
        lines.append(str_row)
    
    return "\n".join(lines)

class ReportGenerator:
    def __init__(self, output_file: str = "log_analysis_results.csv"):
        self.output_file = output_file

    def display_results(self, 
                       ip_counts: List[Tuple[str, int]], 
                       top_endpoint: Tuple[str, int],
                       suspicious_ips: List[Tuple[str, int]]):
        """Display results in a formatted table in the terminal."""
        print("\n=== Requests per IP Address ===")
        print(format_table(ip_counts, ["IP Address", "Request Count"]))

        print("\n=== Most Frequently Accessed Endpoint ===")
        print(f"{top_endpoint[0]} (Accessed {top_endpoint[1]} times)")

        print("\n=== Suspicious Activity Detected ===")
        if suspicious_ips:
            print(format_table(suspicious_ips, ["IP Address", "Failed Login Attempts"]))
        else:
            print("No suspicious activity detected.")

    def save_to_csv(self,
                    ip_counts: List[Tuple[str, int]],
                    top_endpoint: Tuple[str, int],
                    suspicious_ips: List[Tuple[str, int]]):
        """Save analysis results to a CSV file."""
        with open(self.output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            
            # Writing headers and sections
            writer.writerow(["=== Requests per IP ==="])
            writer.writerow(["IP Address", "Request Count"])
            writer.writerows(ip_counts)
            
            writer.writerow([])  # Empty row for separation
            writer.writerow(["=== Most Accessed Endpoint ==="])
            writer.writerow(["Endpoint", "Access Count"])
            writer.writerow(top_endpoint)
            
            writer.writerow([])  # Empty row for separation
            writer.writerow(["=== Suspicious Activity ==="])
            writer.writerow(["IP Address", "Failed Login Count"])
            writer.writerows(suspicious_ips)