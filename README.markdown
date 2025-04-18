# WebWordGen - Advanced Wordlist Generator

**WebWordGen** is a versatile, cross-platform tool built for ethical hacking and penetration testing. It crawls a target website or web application, extracts meaningful words from HTML, attributes, and text, and generates optimized wordlists for security testing. Written in Python, it runs seamlessly on **Termux**, **Kali Linux**, **other Linux distributions**, and **Windows**, making it perfect for security researchers, pentesters, and enthusiasts looking to create custom wordlists.

With an attractive, user-friendly console UI featuring an ASCII banner, colorful panels, and progress bars, WebWordGen is designed to be both powerful and approachable, ideal for beginners and pros alike.

## Features
- **Dynamic Crawling**: Crawls up to 10 pages of a website, extracting words from content, links, and attributes.
- **Word Extraction**: Uses regex to pull words from HTML text, tags, and attributes (e.g., IDs, classes).
- **Customizable Filters**: Set minimum/maximum word lengths and exclude common words (e.g., "the", "is").
- **Proxy Support**: Enable anonymous crawling with proxy servers.
- **Google Drive Integration**: Optionally upload wordlists to Google Drive (requires `pydrive2` library).
- **Attractive UI**: Features an ASCII banner, rich panels, tables, and a styled progress bar for a modern look.
- **Cross-Platform**: Fully compatible with Termux, Kali Linux, other Linux distributions, and Windows.
- **Error Handling**: Logs errors to `output/webwordgen.log` and handles missing dependencies gracefully.
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
- **Python 3.7+**: Install Python from [python.org](https://www.python.org/) (Windows) or your package manager (Linux/Termux).
- **pip**: Python package manager for installing dependencies.
- **Browser**: Required for Google Drive authentication (optional).
- **Internet Connection**: Needed for crawling and installing dependencies.

### 1. Termux
1. **Create Directory Structure**:
   ```bash
   mkdir WebWordGen
   cd WebWordGen
   mkdir output
   ```
2. **Download Files**:
   - Save `webwordgen.py`, `README.md`, `requirements.txt`, `setup.sh`, and `setup.bat` from the repository or copy them manually.
   - Example `requirements.txt`:
     ```
     requests
     aiohttp
     beautifulsoup4
     lxml
     rich
     pydrive2
     ```
   - Make `setup.sh` executable:
     ```bash
     chmod +x setup.sh
     ```
3. **Run Setup**:
   ```bash
   ./setup.sh
   ```
   - Installs Python, pip, and dependencies, and creates the `output` folder.
4. **Optional for Google Drive**:
   - Install `termux-api` for browser authentication:
     ```bash
     pkg install termux-api
     ```

### 2. Kali Linux / Other Linux Distributions
1. **Create Directory Structure**:
   ```bash
   mkdir WebWordGen
   cd WebWordGen
   mkdir output
   ```
2. **Download Files**:
   - Save `webwordgen.py`, `README.md`, `requirements.txt`, `setup.sh`, and `setup.bat`.
   - Make `setup.sh` executable:
     ```bash
     chmod +x setup.sh
     ```
3. **Run Setup**:
   ```bash
   ./setup.sh
   ```
   - May require `sudo` for `apt-get` on Kali/Ubuntu.
   - Installs Python 3, pip, and dependencies.
4. **Optional for Google Drive**:
   - Ensure a browser (e.g., Firefox, Chromium) is installed.

### 3. Windows
1. **Create Directory Structure**:
   - Open Command Prompt or PowerShell:
     ```cmd
     mkdir WebWordGen
     cd WebWordGen
     mkdir output
     ```
2. **Download Files**:
   - Save `webwordgen.py`, `README.md`, `requirements.txt`, `setup.sh`, and `setup.bat` using a text editor (e.g., Notepad).
3. **Run Setup**:
   - Double-click `setup.bat` or run:
     ```cmd
     setup.bat
     ```
   - Ensure Python 3.7+ is installed (download from [python.org](https://www.python.org/) if needed).
   - Installs dependencies and creates the `output` folder.
4. **Optional for Google Drive**:
   - Ensure a default browser (e.g., Chrome, Edge) is installed.

## Usage
1. **Run the Tool**:
   - Navigate to the `WebWordGen` directory.
   - Execute:
     ```bash
     python3 webwordgen.py  # Termux/Linux
     python webwordgen.py   # Windows
     ```
2. **Follow Prompts**:
   - **Show help menu?**: Enter `y` to see a table explaining all options, or `n` to continue.
   - **Enter target URL**: Provide a website URL (e.g., `https://example.com`). The tool adds `https://` if omitted and validates the URL.
   - **Minimum word length**: Set the minimum word length (default: 3). Must be positive.
   - **Maximum word length**: Set the maximum word length (default: 50). Must be ≥ minimum.
   - **Use proxy?**: Enter `y` to use a proxy and provide a proxy URL (e.g., `http://proxy:port`), or `n` for direct connection.
   - **Upload to Google Drive?**: If `pydrive2` is installed, enter `y` to upload the wordlist to Google Drive, or `n` to skip. If `pydrive2` is missing, a warning appears, and the option is disabled.
3. **Output**:
   - The tool displays a colorful ASCII banner and crawls the website, showing a styled progress bar.
   - Words are extracted and saved to `output/wordlist_<timestamp>.txt` (e.g., `wordlist_20250418_124023.txt`).
   - A summary table shows the output file path and word count.
   - Errors are logged to `output/webwordgen.log`.
4. **Google Drive Upload**:
   - If enabled, a browser opens for authentication.
   - In Termux, use `termux-open-url` if prompted to open a link.
   - The wordlist is uploaded as `<timestamp>.txt`.

## Example
```bash
$ python3 webwordgen.py
[ASCII Banner: WebWordGen]
WebWordGen v1.0.0 - Advanced Wordlist Generator
Running on Linux
Created by Muhammad Anas for Ethical Hacking
Subscribe: youtube.com/@YourChannel

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
Upload to Google Drive? (y/n) [n]: y
[Opening browser for authentication...]
[Success: Wordlist uploaded to Google Drive]
[Goodbye: Thank you for using WebWordGen! Subscribe to my YouTube channel!]
```

## Troubleshooting
- **ModuleNotFoundError: No module named 'pydrive2'**:
  - Install `pydrive2`: `pip3 install pydrive2` (Termux/Linux) or `pip install pydrive2` (Windows).
  - If not needed, the tool disables Google Drive upload with a warning.
- **Dependency Issues**:
  - Update pip: `pip install --upgrade pip`.
  - Re-run `pip install -r requirements.txt`.
  - Verify Python environment: `python3 --version` (Termux/Linux) or `python --version` (Windows).
- **Google Drive Authentication**:
  - Termux: Install `termux-api` (`pkg install termux-api`) and use `termux-open-url`.
  - Linux/Windows: Ensure a browser is installed.
- **UI Rendering**:
  - Termux: Set `TERM=xterm-256color` (`export TERM=xterm-256color`).
  - Windows: Use PowerShell or Windows Terminal for better color support.
  - Update `rich`: `pip install --upgrade rich`.
- **Other Errors**:
  - Check `output/webwordgen.log` for details.
  - Ensure internet connectivity for crawling.
  - Verify URL is valid and accessible.

## Contributing
Want to enhance WebWordGen with features like AI-based extraction, custom plugins, or Tor support? Fork the repository, add your changes, and submit a pull request. Check the repository for contribution guidelines.

## License
WebWordGen is released under the MIT License. Use it responsibly for ethical purposes only.

## Contact
Questions or feedback? Join our community on [YouTube](#) or reach out via [email](#). Subscribe for more ethical hacking tutorials and Termux projects!

**Happy Hacking! Stay Ethical!**