# termux-web-vuln-scanner

# Termux Web Vulnerability Scanner

A lightweight, multi-tool website vulnerability scanner designed for **Termux** on Android. It leverages popular open-source tools to perform comprehensive web scans and generate HTML reports.

## 🛠 Tools Integrated

- Nmap
- Nikto
- Dnsenum
- WhatWeb
- Skipfish
- TM-scanner
- TechViper
- Anony-scanner
- WebScan
- Wapiti

## 📦 Installation

```bash
pkg update && pkg upgrade -y
pkg install git -y
git clone https://github.com/YOUR_USERNAME/termux-web-vuln-scanner.git
cd termux-web-vuln-scanner
chmod +x install_tools.sh run_scanner.sh
./install_tools.sh
```

## 🚀 Usage

```bash
./run_scanner.sh
```

Paste the website URL when prompted, and let the scanner run through all tools.

## 📁 Output

- Text reports from each scanner.
- HTML report: `final_report.html`
- Skipfish HTML output: `skipfish_report/index.html`
- Wapiti HTML output: `wapiti_report.html`

## 🔒 Disclaimer

Use only on systems you own or have explicit permission to test. Unauthorized scanning is illegal and unethical.

## ✍️ Credits

Created and maintained by **SDF**.
