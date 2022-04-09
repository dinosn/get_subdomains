# get_subdomains.py
Simple script to get subdomain information given a domain name using securitytrails API

Usage: ```python3 get_subdomains.py example.com ```

The script will generate a list of subdomains found using the API key from securitytrails ( Do create a free account on securitytrails.com and get the API key ).   Upon subdomain retrieval the script will perform a lookup on the subdomains found to ensure that the subdomains resolve into a proper IP.

Two files will be created, one `domain_results.txt` will contain the retrieved information from securitytrails.com and the second `domain_ip.txt` file will contain the valid resolutions.
