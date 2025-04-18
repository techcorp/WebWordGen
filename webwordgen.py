import requests
import aiohttp
import asyncio
import re
from bs4 import BeautifulSoup
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.prompt import Prompt
import logging
from datetime import datetime
from urllib.parse import urljoin
from pathlib import Path
import platform
import sys
import shutil
import os
from concurrent.futures import ThreadPoolExecutor

# Ensure Python 3.7+
if sys.version_info < (3, 7):
    print("Error: Python 3.7 or higher is required.")
    sys.exit(1)

# Initialize rich console
console = Console()

# Tool version
TOOL_VERSION = "1.0.0"

# ASCII banner
ASCII_BANNER = """

 __      __      ___.   __      __                .___________               
/  \    /  \ ____\_ |__/  \    /  \___________  __| _/  _____/  ____   ____  
\   \/\/   _/ __ \| __ \   \/\/   /  _ \_  __ \/ __ /   \  ____/ __ \ /    \ 
 \        /\  ___/| \_\ \        (  <_> |  | \/ /_/ \    \_\  \  ___/|   |  \
  \__/\  /  \___  |___  /\__/\  / \____/|__|  \____ |\______  /\___  |___|  /
       \/       \/    \/      \/                   \/       \/     \/     \/ 
"""

# Setup logging (platform-independent path)
log_dir = Path("output")
log_dir.mkdir(exist_ok=True)
logging.basicConfig(
    filename=log_dir / "webwordgen.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class WebWordGen:
    def __init__(self):
        self.words = set()
        self.urls_crawled = set()
        self.base_url = ""
        self.min_length = 3
        self.max_length = 50
        self.common_words = {'the', 'is', 'and', 'or', 'in', 'to', 'a', 'for'}
        self.regex_patterns = [r'\b\w+\b']
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        self.output_file = self.output_dir / f"wordlist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        self.use_proxy = False
        self.proxy = None
        self.platform = platform.system()
        self.terminal_width = shutil.get_terminal_size().columns

    def display_banner(self):
        """Display ASCII banner and welcome message"""
        banner_text = Text(ASCII_BANNER, style="bold green")
        welcome_message = Text(
            f"WebWordGen v{TOOL_VERSION} - Advanced Wordlist Generator\n"
            f"Running on {self.platform}\n"
            "Created by Technical Corp for Ethical Hacking\n"
            "Subscribe: youtube.com/@technicalcorp2",
            style="bold cyan"
        )
        console.print(Panel(
            banner_text + Text("\n") + welcome_message,
            title="Welcome",
            border_style="blue",
            width=min(self.terminal_width, 80)
        ))

    def display_help(self):
        """Display help menu"""
        help_table = Table(title="WebWordGen Help", width=min(self.terminal_width, 80))
        help_table.add_column("Option", style="cyan")
        help_table.add_column("Description", style="white")
        help_table.add_row("URL", "Enter the target website (e.g., https://example.com)")
        help_table.add_row("Min Length", "Minimum word length (default: 3)")
        help_table.add_row("Max Length", "Maximum word length (default: 50)")
        help_table.add_row("Proxy", "Use a proxy for anonymity (e.g., http://proxy:port)")
        console.print(Panel(
            help_table,
            title="Help Menu",
            border_style="yellow"
        ))

    def setup(self):
        """Setup tool configuration"""
        self.display_banner()
        if Prompt.ask("[bold yellow]Show help menu? (y/n)[/bold yellow]", default="n") == 'y':
            self.display_help()

        console.print(Panel(
            "Enter Configuration Details",
            title="Setup",
            border_style="green",
            width=min(self.terminal_width, 80)
        ))

        # URL input with validation
        while True:
            self.base_url = Prompt.ask("[bold yellow]Enter target URL (e.g., https://example.com)[/bold yellow]")
            if not self.base_url.startswith(('http://', 'https://')):
                self.base_url = 'https://' + self.base_url
            try:
                requests.get(self.base_url, timeout=5)
                break
            except requests.RequestException:
                console.print("[bold red]Invalid or unreachable URL. Please try again.[/bold red]")

        # Word length inputs with validation
        while True:
            try:
                self.min_length = int(Prompt.ask("[bold yellow]Minimum word length[/bold yellow]", default="3"))
                if self.min_length < 1:
                    raise ValueError
                break
            except ValueError:
                console.print("[bold red]Please enter a positive number.[/bold red]")

        while True:
            try:
                self.max_length = int(Prompt.ask("[bold yellow]Maximum word length[/bold yellow]", default="50"))
                if self.max_length < self.min_length:
                    raise ValueError
                break
            except ValueError:
                console.print("[bold red]Max length must be greater than min length.[/bold red]")

        self.use_proxy = Prompt.ask("[bold yellow]Use proxy? (y/n)[/bold yellow]", default="n") == 'y'
        if self.use_proxy:
            self.proxy = Prompt.ask("[bold yellow]Enter proxy (e.g., http://proxy:port)[/bold yellow]")

    async def fetch_page(self, url, session):
        """Fetch webpage content asynchronously"""
        try:
            async with session.get(url, proxy=self.proxy if self.use_proxy else None) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    console.print(f"[bold red]Failed to fetch {url}: Status {response.status}[/bold red]")
                    return None
        except Exception as e:
            logging.error(f"Error fetching {url}: {str(e)}")
            return None

    def extract_words(self, content):
        """Extract words from content"""
        if not content:
            return

        # Parse with BeautifulSoup using html.parser
        soup = BeautifulSoup(content, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        
        # Extract words using regex
        for pattern in self.regex_patterns:
            matches = re.findall(pattern, text)
            for word in matches:
                if (self.min_length <= len(word) <= self.max_length and 
                    word.lower() not in self.common_words and word.isascii()):
                    self.words.add(word)

        # Extract from attributes
        for tag in soup.find_all(True):
            for attr in tag.attrs.values():
                if isinstance(attr, str):
                    words = re.findall(r'\b\w+\b', attr)
                    for word in words:
                        if (self.min_length <= len(word) <= self.max_length and 
                            word.lower() not in self.common_words and word.isascii()):
                            self.words.add(word)

    def crawl(self, max_pages=10):
        """Crawl the website and extract words"""
        self.urls_crawled.add(self.base_url)
        urls_to_crawl = [self.base_url]
        fetched_pages = 0

        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=min(self.terminal_width // 2, 40)),
            "[progress.percentage]{task.percentage:>3.0f}%",
            TimeRemainingColumn(),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Crawling...", total=max_pages)

            async def fetch_all():
                nonlocal fetched_pages
                async with aiohttp.ClientSession() as session:
                    while urls_to_crawl and fetched_pages < max_pages:
                        url = urls_to_crawl.pop(0)
                        content = await self.fetch_page(url, session)
                        if content:
                            self.extract_words(content)
                            soup = BeautifulSoup(content, 'html.parser')
                            for link in soup.find_all('a', href=True):
                                href = link['href']
                                full_url = urljoin(self.base_url, href)
                                if (full_url.startswith(self.base_url) and 
                                    full_url not in self.urls_crawled and 
                                    full_url not in urls_to_crawl):
                                    urls_to_crawl.append(full_url)
                                    self.urls_crawled.add(full_url)
                            fetched_pages += 1
                            progress.update(task, advance=1)

            asyncio.run(fetch_all())

    def save_wordlist(self):
        """Save wordlist to file"""
        with self.output_file.open('w', encoding='utf-8') as f:
            for word in sorted(self.words):
                f.write(word + '\n')
        summary = Table(title="Wordlist Summary", width=min(self.terminal_width, 80))
        summary.add_column("Field", style="cyan")
        summary.add_column("Value", style="white")
        summary.add_row("File", str(self.output_file))
        summary.add_row("Words", str(len(self.words)))
        console.print(Panel(
            summary,
            title="Success",
            border_style="green"
        ))

    def run(self):
        """Run the tool"""
        try:
            self.setup()
            self.crawl()
            self.save_wordlist()
            console.print(Panel(
                "Thank you for using WebWordGen!\n"
                "Subscribe to my YouTube channel for more ethical hacking tools!",
                title="Goodbye",
                border_style="blue",
                width=min(self.terminal_width, 80)
            ))
        except KeyboardInterrupt:
            console.print(Panel(
                "Operation cancelled by user.",
                title="Stopped",
                border_style="yellow",
                width=min(self.terminal_width, 80)
            ))
        except Exception as e:
            console.print(Panel(
                f"An error occurred: {str(e)}",
                title="Error",
                border_style="red",
                width=min(self.terminal_width, 80)
            ))
            logging.error(f"Runtime error: {str(e)}")

if __name__ == "__main__":
    tool = WebWordGen()
    tool.run()
