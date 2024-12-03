"""Main script for log analysis"""
import sys
from log_parser import read_log_file
from log_analyzer import LogAnalyzer
from report_generator import ReportGenerator

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]
    
    try:
        # Here we are Parsing log file
        print("Reading log file...")
        log_entries = read_log_file(log_file)
        
        # Here we are Analyzing logs
        print("Analyzing logs...")
        analyzer = LogAnalyzer(log_entries)
        ip_counts = analyzer.count_requests_per_ip()
        top_endpoint = analyzer.find_most_accessed_endpoint()
        suspicious_ips = analyzer.detect_suspicious_activity()
        
        # Here we are Generating reports
        print("\nGenerating reports...")
        reporter = ReportGenerator()
        reporter.display_results(ip_counts, top_endpoint, suspicious_ips)
        reporter.save_to_csv(ip_counts, top_endpoint, suspicious_ips)
        print(f"\nResults have been saved to {reporter.output_file}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


#CreatedByTejasGupta    