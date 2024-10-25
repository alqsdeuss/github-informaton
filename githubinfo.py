import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import time
import sys

a = "ur token"
base_url = "https://api.github.com/users"
console = Console()

def get_user_info(username):
    headers = {}
    if a:
        headers['Authorization'] = f'token {a}'
    
    response = requests.get(f"{base_url}/{username}", headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def loading_animation(duration=3):
    end_time = time.time() + duration
    while time.time() < end_time:
        for symbol in ["|", "/", "-", "\\"]:
            sys.stdout.write(f"\r{symbol}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * 30 + "\r")

def display_user_info(data, username):
    table = Table(title=f"user info for {data['login']}", style="bold magenta")
    table.add_column("attribute", style="cyan", no_wrap=True)
    table.add_column("value", style="green")
    
    table.add_row("username", data.get('login', 'N/A'))
    table.add_row("name", data.get('name', 'N/A'))
    table.add_row("email", data.get('email', 'N/A') if data.get('email') else 'N/A')
    table.add_row("followers", str(data.get('followers', 'N/A')))
    table.add_row("following", str(data.get('following', 'N/A')))
    table.add_row("public repos", str(data.get('public_repos', 'N/A')))
    table.add_row("public gists", str(data.get('public_gists', 'N/A')))
    table.add_row("bio", data.get('bio') if data.get('bio') else 'N/A')
    table.add_row("created at", data.get('created_at', 'N/A'))
    table.add_row("update at", data.get('updated_at', 'N/A'))
    console.print(table)

def main():
    console.print(Panel("follow me on github now (type [bold cyan]exit[/bold cyan] to quit)", style="bold magenta"))
    while True:
        username = console.input("\n[bold magenta]enter a github username:[/bold magenta] ")
        if username.lower() == "exit":
            console.print("[bold black]bye nigga[/bold black]") 
            break
        loading_animation()
        data = get_user_info(username)
        if data:
            display_user_info(data, username)
        else:
            console.print(f"[bold red]huh?[/bold red] '{username}' is not a valid github username")

if __name__ == "__main__":
    main()
