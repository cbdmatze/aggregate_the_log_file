import re
from collections import defaultdict

def extract_main_domain(domain):
    """
    Extracts the main domain from a full domain name, accounting for special .co.xx or .com.xx cases.
    """
    parts = domain.split('.')
    
    # Special case for domains like .co.xx or .com.xx
    if len(parts) >= 3 and parts[-2] in ['co', 'com']:
        return '.'.join(parts[-3:])
    
    # Otherwise, take the last two parts
    return '.'.join(parts[-2:])

def count_domains(log_file, min_hits=0):
    """Aggregates domain hits from a log file, and filters by min_hits."""

    # Dictionary to store the aggregated hits for each main domain
    domain_hits = defaultdict(int)

    # Parse the log file, extracting each line
    lines = log_file.strip().split('\n')

    for line in lines:
        # Use regex to separate the domain and the number of hits
        match = re.match(r'([\w\.-]+)\s+(\d+)', line)
        if match:
            domain = match.group(1).strip('*.') # Remove leading * and strip spaces
            hits = int(match.group(2))

            # Extract the main domain
            main_domain = extract_main_domain(domain)

            # Add the hits to the main domain
            domain_hits[main_domain] += hits

    # Filter by min_hits and sort by hits in descending order, then alphabetically for ties
    filtered_domains = {domain: hits for domain, hits in domain_hits.items() if hits >= min_hits}
    sorted_domains = sorted(filtered_domains.items(), key=lambda x: (-x[1], x[0]))

    # Format the result as a string, each domain on a new line
    result = '\n'.join([f"{domain} ({hits})" for domain, hits in sorted_domains])

    return result

# Example usage:

log_file = """
*.amazon.co.uk    89
*.doubleclick.net    139
*.fbcdn.net    212
*.in-addr.arpa    384
*.l.google.com    317
1.client-channel.google.com    110
6.client-channel.google.com    45
a.root-servers.net    1059
apis.google.com    43
clients4.google.com    71
clients6.google.com    81
connect.facebook.net    68
edge-mqtt.facebook.com    56
graph.facebook.com    150
mail.google.com    128
mqtt-mini.facebook.com    47
ssl.google-analytics.com    398
star-mini.c10r.facebook.com    46
staticxx.facebook.com    48
www.facebook.com    178
www.google.com    162
www.google-analytics.com    127
www.googleapis.com    87
"""

# Example call to count_domains function
print(count_domains(log_file, 50))
