vuln_scanner.py

import os import subprocess from urllib.parse import urlparse

def print_banner(): banner = r'''


---

/ |  __ _   | | ( | |  | || |
_ | |  | || |
___) | |__| || | |/|/_____|

Web Vuln Scanner
    By SDF

''' print(banner)

def run_command(command, output_file): print(f"\n[+] Running: {command}") with open(output_file, 'w') as out: subprocess.run(command, shell=True, stdout=out, stderr=subprocess.STDOUT)

def nmap_scan(target): run_command(f"nmap -sC -sV -O {target}", "nmap_report.txt")

def nikto_scan(url): run_command(f"nikto -host {url}", "nikto_report.txt")

def dns_enum(domain): run_command(f"dnsenum {domain}", "dnsenum_report.txt")

def whatweb_scan(url): run_command(f"whatweb {url}", "whatweb_report.txt")

def skipfish_scan(url): run_command(f"skipfish -o skipfish_report {url}", os.devnull)

def tm_scanner(url): run_command(f"cd TM-scanner && python2 tm-scanner.py {url}", "tm_scanner_report.txt")

def techviper(url): run_command(f"cd TechViper && python3 techviper.py -u {url}", "techviper_report.txt")

def anony_scanner(url): run_command(f"cd anony-scanner && python2 anony-scanner.py {url}", "anony_scanner_report.txt")

def webscan(url): run_command(f"cd WebScan && python3 webscan.py {url}", "webscan_report.txt")

def wapiti_scan(url): run_command(f"wapiti -u {url} -f html -o wapiti_report.html", os.devnull)

def generate_html_report(): print("\n[+] Generating HTML report...\n") html_content = "<html><head><title>Vulnerability Scan Report</title></head><body><h1>Vulnerability Scan Results</h1>" for report in ["nmap_report.txt", "nikto_report.txt", "dnsenum_report.txt", "whatweb_report.txt", "tm_scanner_report.txt", "techviper_report.txt", "anony_scanner_report.txt", "webscan_report.txt"]: if os.path.exists(report): with open(report, 'r') as f: content = f.read().replace("\n", "<br>") html_content += f"<h2>{report}</h2><pre>{content}</pre>" html_content += "<h2>Skipfish Report</h2><p>Open <a href='skipfish_report/index.html'>skipfish_report/index.html</a> for detailed HTML report.</p>" html_content += "<h2>Wapiti Report</h2><p>Open <a href='wapiti_report.html'>wapiti_report.html</a> for Wapiti scan results.</p>" html_content += "</body></html>"

with open("final_report.html", "w") as f:
    f.write(html_content)

print("\n[+] HTML report saved as 'final_report.html'")

def open_html_report(): print("\n[+] Opening HTML report in Termux browser (w3m)...") os.system("w3m final_report.html")

def main(): print_banner() url = input("Enter the target website URL (e.g., http://example.com): ").strip() parsed = urlparse(url) hostname = parsed.hostname or url

print(f"[+] Starting scans for: {hostname}")

nmap_scan(hostname)
nikto_scan(url)
dns_enum(hostname)
whatweb_scan(url)
skipfish_scan(url)
tm_scanner(url)
techviper(url)
anony_scanner(url)
webscan(url)
wapiti_scan(url)

generate_html_report()
open_html_report()

if name == "main": main()
