"""Module for parsing log file entries."""
import re
from typing import List, Dict, Tuple
from dataclasses import dataclass
from datetime import datetime

@dataclass
class LogEntry:
    ip_address: str
    timestamp: datetime
    method: str
    endpoint: str
    status_code: int
    response_size: int
    message: str = ""

def parse_log_line(line: str) -> LogEntry:
    """Parse a single log line into a LogEntry object."""
    pattern = r'(\d+\.\d+\.\d+\.\d+).*\[(.*?)\]\s+"(\w+)\s+([^\s]+)[^"]+"\s+(\d+)\s+(\d+)(?:\s+"([^"]*)")?'
    match = re.match(pattern, line)
    
    if not match:
        raise ValueError(f"Invalid log line format: {line}")
        
    ip, timestamp_str, method, endpoint, status, size, message = match.groups()
    timestamp = datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S %z")
    
    return LogEntry(
        ip_address=ip,
        timestamp=timestamp,
        method=method,
        endpoint=endpoint,
        status_code=int(status),
        response_size=int(size),
        message=message if message else ""
    )

def read_log_file(filename: str) -> List[LogEntry]:
    """Read and parse the log file."""
    entries = []
    with open(filename, 'r') as f:
        for line in f:
            try:
                entry = parse_log_line(line.strip())
                entries.append(entry)
            except ValueError as e:
                print(f"Warning: {e}")
    return entries