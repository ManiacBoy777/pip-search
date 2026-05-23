#!/usr/bin/env python3
"""
Simple PyPI package search tool with enhanced styling and hyperlinking.
Usage: pip-search-two <search_terms...> [-n COUNT]
"""

import sys
import requests
import re
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

# ANSI escape codes for styling
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

def create_hyperlink(text, url):
    """Create a terminal hyperlink if supported"""
    return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"

def get_package_info(package_name):
    """Get package description from PyPI JSON API"""
    try:
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=3)
        if response.status_code == 200:
            data = response.json()
            info = data.get('info', {})
            summary = info.get('summary', 'No description available')
            version = info.get('version', '?.?.?')
            # Clean up the summary
            if summary:
                summary = summary.strip()[:100]  # Limit to 100 chars
            else:
                summary = 'No description available'
            return {"summary": summary, "version": version}
        return {"summary": 'No description available', "version": "unknown"}
    except:
        return {"summary": 'No description available', "version": "unknown"}

def search_packages(term):
    """Search PyPI simple index for packages"""
    try:
        response = requests.get("https://pypi.org/simple/", timeout=10)
        if response.status_code != 200:
            return []
        
        # Extract package names
        packages = re.findall(r'<a href="/simple/([^/]+)/">', response.text)
        
        # Handle multiple search terms
        search_words = term.lower().split()
        
        # Search for packages containing any of the terms in their name
        matches = []
        for pkg in packages:
            pkg_lower = pkg.lower()
            if any(word in pkg_lower for word in search_words):
                matches.append(pkg)
        
        # Prioritize exact matches and shorter names
        def sort_key(pkg):
            pkg_lower = pkg.lower()
            if pkg_lower == term.lower():
                return (0, len(pkg))
            if term.lower() in pkg_lower:
                return (1, len(pkg))
            return (2, len(pkg))
            
        matches.sort(key=sort_key)
        return matches
    
    except Exception as e:
        print(f"Error searching packages: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(
        description="Search PyPI packages with styled output and description search",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s requests
  %(prog)s machine learning
  %(prog)s web scraping -n 20
        """
    )
    
    parser.add_argument(
        'search_terms',
        nargs='+',
        help='Search terms (multiple words will be joined with spaces)'
    )
    
    parser.add_argument(
        '-n', '--count',
        type=int,
        default=10,
        help='Number of results to show (default: 10)'
    )
    
    args = parser.parse_args()
    
    # Join multiple search terms with spaces
    search_term = ' '.join(args.search_terms)
    search_words = search_term.lower().split()
    
    # Search for packages by name first
    name_matches = search_packages(search_term)
    
    if not name_matches:
        print(f"{YELLOW}No packages found matching names.{RESET}")
        return
    
    # Limit initial name matches to a reasonable number to check descriptions
    # We check more than 'count' to allow for description-based filtering/ranking
    check_count = max(args.count * 3, 100)
    packages_to_check = name_matches[:check_count]
    
    # Get descriptions concurrently
    package_info = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_pkg = {executor.submit(get_package_info, pkg): pkg for pkg in packages_to_check}
        for future in as_completed(future_to_pkg):
            pkg = future_to_pkg[future]
            try:
                package_info[pkg] = future.result()
            except:
                package_info[pkg] = {"summary": 'No description available', "version": "unknown"}
    
    # Ranking function: prioritize exact name match, then name contains, then description contains
    def get_score(pkg):
        pkg_lower = pkg.lower()
        info = package_info.get(pkg, {})
        desc_lower = info.get('summary', '').lower()
        
        score = 0
        if pkg_lower == search_term.lower():
            score += 5000
        
        # Exact word match in name is better than partial
        for word in search_words:
            if word == pkg_lower:
                score += 2000
            elif word in pkg_lower:
                score += 500
            
            if word in desc_lower:
                score += 100
        
        # Shorter names are usually more relevant for the base package
        score -= len(pkg) 
        
        return score

    # Sort by score descending
    sorted_packages = sorted(package_info.keys(), key=lambda p: -get_score(p))
    
    # Display results
    results_shown = 0
    for pkg in sorted_packages:
        if results_shown >= args.count:
            break
            
        info = package_info.get(pkg, {})
        summary = info.get('summary', 'No description available')
        version = info.get('version', 'unknown')
        url = f"https://pypi.org/project/{pkg}/"
        
        # Style the output
        styled_pkg = f"{BOLD}{BLUE}{create_hyperlink(pkg, url)}{RESET}"
        styled_version = f"{GREEN}{version}{RESET}"
        
        # Mark exact matches with a star
        is_exact = pkg.lower() == search_term.lower()
        prefix = f"{YELLOW}*{RESET} " if is_exact else "  "
        
        print(f"{prefix}{styled_pkg} ({styled_version}) - {summary}")
        results_shown += 1

    if results_shown == 0:
        print(f"{YELLOW}No packages found.{RESET}")

if __name__ == "__main__":
    main()
