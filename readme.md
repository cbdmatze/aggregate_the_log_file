
🌐 Domain Access Log Aggregator

This Python program aggregates domain access requests from a log file, reducing subdomains into their main domain and counting the total number of access requests. The output is sorted by the number of requests in descending order, with an option to filter out domains that don't meet a minimum hit count. It’s perfect for processing large logs where you want to consolidate all hits to main domains (e.g., google.com, facebook.com).



Features ✨

Domain Aggregation: Aggregates hits from subdomains to the main domain (e.g., mail.google.com and apis.google.com both count towards google.com).
Special Domain Handling: Domains with formats like amazon.co.uk or example.com.br are correctly handled to maintain three levels.
Hit Filtering: Optionally filter out domains with fewer than a specified number of hits.
Sorted Output: Results are sorted in descending order by number of hits. If domains have the same number of hits, they are sorted alphabetically.
Simple and Readable Output: Displays domains in a neat format with their total hits, ready for reports or further analysis.



Example 📄
Given the following log file:

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

If you want to count only domains that have more than 500 hits, the program output would be:

root-servers.net (1059)
google.com (957)
facebook.com (525)
google-analytics.com (525)



Installation and Requirements 💻

The program is written in Python and does not require any external libraries, making it lightweight and easy to run in any Python environment.



To run the program:

Make sure you have Python 3.x installed.
Download or clone this repository.
Copy your log data into the log_file variable (or read it from an actual file, if you wish to extend the program).



How It Works 🔍

Log Parsing: The program processes each line of the log, extracts the domain and the number of hits, and strips subdomains down to their main domain.

Aggregation: Using Python’s defaultdict, the hits from each subdomain are summed into their main domain.

Sorting & Filtering: Results are sorted by total hits (descending) and filtered based on a customizable min_hits threshold.

Special Domain Handling: Certain domains (like .co.xx or .com.xx) retain three levels, while others default to two levels.



Usage ⚙️

def count_domains(log_file, min_hits=0):
    # log_file: A string representing the log file contents.
    # min_hits: An optional integer to filter out domains with fewer than this number of hits.
    pass  # (the program code goes here)

log_file = """
*.amazon.co.uk    89
*.doubleclick.net    139
*.fbcdn.net    212


# Call the function with a log file and a minimum hit count
print(count_domains(log_file, 500))

Output:

root-servers.net (1059)
google.com (957)
facebook.com (525)
google-analytics.com (525)



Customization 🛠️

You can easily tweak the following parts:

Minimum hit threshold: The second argument in the count_domains() function allows you to set a custom minimum hit count (min_hits).

Log file source: Currently, the log file is a string passed directly into the function. You can extend this to read from an actual file if needed.



Example Use Cases 🚀

Log Analysis: This program is perfect for analyzing server logs to see which main domains are receiving the most traffic.

Data Aggregation: Useful for aggregating website access logs by domain for web traffic reporting.
Security and Performance Monitoring: Can help in identifying the most frequently accessed domains to optimize resources or enhance security.



Future Enhancements 🔮

Add support for input directly from a file.
Implement further domain customization (e.g., defining custom domain handling rules).
Optimize performance for large-scale logs.



License 📜

This project is open-source and available under the MIT License.

Enjoy aggregating your log files! 🎉