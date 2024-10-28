from collections import defaultdict

LOG_FILE_CONTENT = """
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

def count_domains(log_file, min_hits=0):
    # Create a dictionary to hold the counts
    domain_counts = defaultdict(int)
    
    # Split the log file into lines and process each line
    for line in log_file.strip().splitlines():
        # Split the line by whitespace to get domain and count
        parts = line.split()
        if len(parts) == 2:
            domain = parts[0].lstrip('*')  # Remove leading '*' if present
            count = int(parts[1])  # Convert count to integer
            domain_counts[domain] += count  # Accumulate counts

    # Filter domains by minimum hits and format output
    filtered_domains = {domain: count for domain, count in domain_counts.items() if count >= min_hits}

    # Process and format output
    result = []
    for domain, count in sorted(filtered_domains.items(), key=lambda x: (-x[1], x[0])):
        result.append(f"{domain} ({count})")

    return "\n".join(result)

def main():
    result = count_domains(LOG_FILE_CONTENT, min_hits=100)
    print(result)

if __name__ == "__main__":
    main()
