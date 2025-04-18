# WebWordGen - Advanced Wordlist Generator

**WebWordGen** is a powerful, cross-platform Python tool designed for ethical hacking and penetration testing. It crawls a target website, extracts meaningful words from HTML content, attributes, and links, and generates optimized wordlists for security testing. With a vibrant, user-friendly console UI featuring an ASCII banner, colorful panels, and a styled progress bar, WebWordGen runs seamlessly on **Termux**, **Kali Linux**, **other Linux distributions**, and **Windows**, making it ideal for security researchers, pentesters, and enthusiasts.

## Description
WebWordGen is a cross-platform Python tool for ethical hacking, generating wordlists by crawling websites and extracting words from HTML content. With a user-friendly UI, it supports Termux, Kali Linux, other Linux distributions, and Windows, ideal for penetration testing with permission.

## Features
- **Dynamic Crawling**: Crawls up to 10 pages of a website, extracting words from HTML text, links, and attributes.
- **Word Extraction**: Uses regex to pull words from HTML content and tags (e.g., IDs, classes).
- **Customizable Filters**: Set minimum/maximum word lengths and exclude common words (e.g., "the", "is").
- **Proxy Support**: Enable anonymous crawling with proxy servers.
- **Attractive UI**: Features an ASCII banner, rich panels, tables, and a progress bar for a modern, engaging experience.
- **Cross-Platform**: Compatible with Termux, Kali Linux, other Linux distributions, and Windows.
- **Error Handling**: Logs errors to `output/webwordgen.log` for easy debugging.
- **User-Friendly**: Includes input validation, a help menu, and clear feedback for all actions.

## Ethical Use
WebWordGen is intended for **ethical hacking** and **penetration testing** with explicit permission from the website owner. Unauthorized crawling or testing is illegal and unethical. Always obtain consent before using this tool on any website.

## File Structure
```
/WebWordGen
├── /output             # Generated wordlists and logs
│   ├── wordlist_<timestamp>.txt # Generated wordlist files
│   └── webwordgen.log  # Log file for errors
├── webwordgen.py       # Main script with enhanced UI
├── README.md           # This documentation
├── requirements.txt    # Python dependencies
├── setup.sh            # Setup script for Termux/Linux
└── setup.bat           # Setup script for Windows
```

## Installation

### Prerequisites
- **Python 3.7+**: Install from [python.org](https://www.python.org/) (Windows) or your package manager (Linux/Termux).
- **pip**: Python package manager for installing dependencies.
- **Git**: Required to clone the repository.
- **Internet Connection**: Needed for cloning, installing dependencies, and crawling websites.

### 1. Termux
1. **Install Prerequisites**:
   ```bash
   pkg update && pkg upgrade
   pkg install python git
   ```
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/WebWordGen.git
   cd WebWordGen
   ```
3. **Run Setup**:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
   - Installs dependencies (`requests`, `aiohttp`, `beautifulsoup4`, `lxml`, `rich`) and creates the `output` folder.
4. **Run the Tool**:
   ```bash
   python3 webwordgen.py
   ```

### 2. Kali Linux / Other Linux Distributions
1. **Install Prerequisites**:
   ```bash
   sudo apt-get update
   sudo apt-get install -y python3 python3-pip git
   ```
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/WebWordGen.git
   cd WebWordGen
   ```
3. **Run Setup**:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
   - Installs dependencies and creates the `output` folder. May require `sudo` for `pip`.
4. **Run the Tool**:
   ```bash
   python3 webwordgen.py
   ```

### 3. Windows
1. **Install Prerequisites**:
   - Download and install **Python 3.7+** from [python.org](https://www.python.org/). Ensure `pip` is added to PATH.
   - Install **Git** from [git-scm.com](https://git-scm.com/) or use Git Bash.
2. **Clone the Repository**:
   - Open Command Prompt, PowerShell, or Git Bash:
     ```cmd
     git clone https://github.com/techcorp/WebWordGen.git
     cd WebWordGen
     ```
3. **Run Setup**:
   - Double-click `setup.bat` or run:
     ```cmd
     setup.bat
     ```
   - Installs dependencies and creates the `output` folder.
4. **Run the Tool**:
   ```cmd
   python webwordgen.py
   ```

## Usage
1. **Run the Tool**:
   - Navigate to the `WebWordGen` directory.
   - Execute:
     ```bash
     python3 webwordgen.py  # Termux/Linux
     python webwordgen.py   # Windows
     ```
2. **Follow Prompts**:
   - **Show help menu?**: Enter `y` to view a table explaining options (URL, word lengths, proxy), or `n` to proceed.
   - **Enter target URL**: Provide a website URL (e.g., `https://example.com`). The tool adds `https://` if omitted and validates the URL.
   - **Minimum word length**: Set the minimum word length (default: 3). Must be positive.
   - **Maximum word length**: Set the maximum word length (default: 50). Must be ≥ minimum.
   - **Use proxy?**: Enter `y` to use a proxy and provide a proxy URL (e.g., `http://proxy:port`), or `n` for direct connection.
3. **Output**:
   - The tool displays a colorful ASCII banner and crawls the website, showing a styled progress bar.
   - Words are extracted and saved to `output/wordlist_<timestamp>.txt` (e.g., `wordlist_20250418_124023.txt`).
   - A summary table displays the output file path and word count.
   - Errors are logged to `output/webwordgen.log`.

## Example
```bash
$ python3 webwordgen.py
[ASCII Banner: WebWordGen]
WebWordGen v1.0.0 - Advanced Wordlist Generator
Running on Linux
Created by Muhammad Anas for Ethical Hacking
Subscribe: youtube.com/@technicalcorp2

Show help menu? (y/n) [n]: n
Enter Configuration Details
Enter target URL (e.g., https://example.com): example.com
Minimum word length [3]: 3
Maximum word length [50]: 50
Use proxy? (y/n) [n]: n
Crawling... [██████████] 100% [Time Remaining: 00:00]
[Success: Wordlist Summary]
  File: output/wordlist_20250418_124023.txt
  Words: 150
[Goodbye: Thank you for using WebWordGen! Subscribe to my YouTube channel!]
```

## Troubleshooting
- **Dependency Issues**:
  - Update pip: `pip install --upgrade pip`.
  - Re-run `pip install -r requirements.txt`.
  - Verify Python environment: `python3 --version` (Termux/Linux) or `python --version` (Windows).
- **UI Rendering**:
  - Termux: Set `TERM=xterm-256color` (`export TERM=xterm-256color`).
  - Windows: Use PowerShell or Windows Terminal for better color support.
  - Update `rich`: `pip install --upgrade rich`.
- **Git Issues**:
  - Ensure Git is installed: `git --version`.
  - Verify repository URL: `git clone https://github.com/techcorp/WebWordGen.git`.
- **Other Errors**:
  - Check `output/webwordgen.log` for details.
  - Ensure internet connectivity for cloning and crawling.
  - Verify URL is valid and accessible.

## Contributing
Want to add features like AI-based extraction, custom plugins, or Tor support? Fork the repository, make changes, and submit a pull request. See the repository for contribution guidelines.

## License
WebWordGen is released under the MIT License. Use it responsibly for ethical purposes only.

## Contact
Questions or feedback? Join our community on [YouTube](#) or reach out via [email](#). Subscribe for more ethical hacking tutorials and Termux projects!

**Happy Hacking! Stay Ethical!**
