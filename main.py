import os
import sys
import shutil
import tempfile
from datetime import datetime, timedelta
import time
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich import print as rprint
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from colorama import init, Fore, Style

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rainbow_print(text, delay=0.001):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for i, char in enumerate(text):
        if char != '\n':
            sys.stdout.write(f"{colors[i % len(colors)]}{char}{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(delay)
        else:
            print()

def load_ascii_art():
    try:
        with open("Boost/asscii/title.txt", "r") as f:
            return f.read()
    except:
        return """
  ________.__  __    __________                       __    
 /  _____/|__|/  |_  \______   \ ____   ____  _______/  |_  
/   \  ___|  \   __\  |    |  _//  _ \ /  _ \/  ___/\   __\ 
\    \_\  \  ||  |    |    |   (  <_> |  <_> )___ \  |  |   
 \______  /__||__|    |______  /\____/ \____/____  > |__|   
        \/                   \/                  \/         
        """

def display_welcome():
    clear_screen()
    ascii_art = load_ascii_art()
    rainbow_print(ascii_art)
    
    welcome_text = """
    🚀 Welcome to GitBoost - Supercharge Your GitHub Contributions! 🚀
    
    ✨ Boost your GitHub activity with style ✨
    📊 Customize your contribution graph 📊
    🎯 Set your own commit schedule 🎯
    
    [dim]Created with ❤️ by the GitBoost Team[/dim]
    """
    console.print(Panel(welcome_text, style="bold cyan", border_style="green"))
    time.sleep(0.5)

def format_date_range(start_date, end_date):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    
    if start_date.year == end_date.year and start_date.month == end_date.month:
        return f"{start_date.day}-{end_date.day} {months[start_date.month-1]} {start_date.year}"
    elif start_date.year == end_date.year:
        return f"{start_date.day} {months[start_date.month-1]} - {end_date.day} {months[end_date.month-1]} {start_date.year}"
    else:
        return f"{start_date.day} {months[start_date.month-1]} {start_date.year} - {end_date.day} {months[end_date.month-1]} {end_date.year}"

def get_user_input():
    console.print("\n[bold yellow]🔧 Configuration Settings[/bold yellow]", style="bold")
    
    # Get repository URL
    repo_link = Prompt.ask("\n[cyan]📁 Enter your repository SSH URL[/cyan]", 
                          default="git@github.com:username/repo.git")
    while not repo_link.startswith("git@github.com:"):
        console.print("[red]❌ Invalid SSH URL format. Please try again.[/red]")
        repo_link = Prompt.ask("[cyan]📁 Enter your repository SSH URL[/cyan]")

    # Get GitHub email
    git_email = Prompt.ask("\n[cyan]👤 Enter your GitHub email[/cyan] [dim](same as in GitHub settings)[/dim]")
    while not ("@" in git_email and "." in git_email):
        console.print("[red]❌ Invalid email format. Please try again.[/red]")
        git_email = Prompt.ask("[cyan]👤 Enter your GitHub email[/cyan]")

    # Get date range
    console.print("\n[bold yellow]📅 Commit Date Range[/bold yellow]")
    console.print("[dim]Format: YYYY-MM-DD (e.g., 2024-01-01)[/dim]")
    
    while True:
        try:
            start_date = datetime.strptime(
                Prompt.ask("[cyan]📅 Enter start date[/cyan]"),
                "%Y-%m-%d"
            ).date()
            break
        except ValueError:
            console.print("[red]❌ Invalid date format. Please use YYYY-MM-DD[/red]")

    while True:
        try:
            end_date = datetime.strptime(
                Prompt.ask("[cyan]📅 Enter end date[/cyan]"),
                "%Y-%m-%d"
            ).date()
            if end_date >= start_date:
                break
            console.print("[red]❌ End date must be after start date[/red]")
        except ValueError:
            console.print("[red]❌ Invalid date format. Please use YYYY-MM-DD[/red]")

    # Get commit frequency
    commit_freq = int(Prompt.ask(
        "\n[cyan]🔄 Enter commits per day[/cyan] [1-10]",
        choices=[str(i) for i in range(1, 11)],
        default="3"
    ))

    return repo_link, git_email, start_date, end_date, commit_freq

def create_temp_repo():
    temp_base = tempfile.gettempdir()
    temp_dir = os.path.join(temp_base, f'gitboost_{int(time.time())}')
    os.makedirs(temp_dir, exist_ok=True)
    return temp_dir

def main():
    original_dir = os.getcwd()
    temp_dir = None
    
    try:
        display_welcome()
        repo_link, git_email, start_date, end_date, commit_freq = get_user_input()
        
        console.print("\n[bold green]🚀 Press Enter to begin the boost...[/bold green]")
        input()

        # Create and move to temporary directory
        temp_dir = create_temp_repo()
        os.chdir(temp_dir)
        
        # Initialize repository with user's email
        os.system("git init")
        os.system(f'git config user.name "GitBoost"')
        os.system(f'git config user.email "{git_email}"')
        
        # Calculate total days and commits
        total_days = (end_date - start_date).days + 1
        total_commits = total_days * commit_freq
        commits_made = 0
        
        with Progress(
            "[progress.description]{task.description}",
            SpinnerColumn("dots"),
            BarColumn(complete_style="green", finished_style="bold green"),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            console=console,
            transient=True
        ) as progress:
            
            boost_task = progress.add_task(
                "[bold cyan]🔥 Boosting your GitHub activity...", 
                total=total_commits
            )

            # Start from start_date and move forward
            current_date = start_date
            while current_date <= end_date:
                for commit_num in range(commit_freq):
                    if commits_made >= total_commits:
                        break
                        
                    formatdate = current_date.strftime("%Y-%m-%d")
                    commit_time = "12:15:10"
                    
                    # Create commit entry
                    with open("commit.txt", "a+") as f:
                        f.write(f"commit {commits_made + 1}: {formatdate}\n")
                    
                    # Add and commit with specific date
                    os.system("git add commit.txt")
                    commit_cmd = f'git commit --date="{formatdate} {commit_time}" -m "commit {commits_made + 1}"'
                    os.system(commit_cmd)
                    
                    commits_made += 1
                    progress.update(boost_task, advance=1)
                    time.sleep(0.1)
                
                current_date += timedelta(days=1)
            
            # Setup remote and push
            os.system(f"git remote add origin {repo_link}")
            os.system("git branch -M main")
            
            console.print("\n[yellow]📤 Pushing commits to repository...[/yellow]")
            push_result = os.system("git push -u origin main -f")
            
            if push_result == 0:
                date_range = format_date_range(start_date, end_date)
                success_text = f"""
                ✨ Success! Your GitHub activity has been boosted! ✨
                
                📅 Commits added for: {date_range}
                📊 Total commits: {commits_made}
                🎯 Commits per day: {commit_freq}
                
                [bold yellow]🤝 Need Support?[/bold yellow]
        
                🌐 Website: https://gitboost.org
                📧 Email: info@gitboost.org
                💻 GitHub: https://github.com/Audran-wol/gitboost
                
                [bold magenta]💝 Support Developer[/bold magenta]
                If you find GitBoost helpful, consider supporting the developer:
                💰 Donate: https://skrill.me/rq/Tiedang%20Yematha/5.00/EUR?key=E6Mu-Z-pyjnRej923zl53Rohtzt
                
                [bold cyan]Thank you for using GitBoost! 🚀[/bold cyan]
                """
                console.print(Panel(success_text, 
                                 title="[bold green]Boost Complete![/bold green]",
                                 border_style="green"))
            else:
                error_text = """
                ❌ Failed to push commits. Please check:
                
                1. Your repository URL is correct
                2. You have write access to the repository
                3. Your SSH key is properly set up
                4. Your GitHub email is verified
                
                Need help? Visit our GitHub repository for troubleshooting guides.
                """
                console.print(Panel(error_text, 
                                 title="[bold red]Error[/bold red]",
                                 border_style="red"))
                
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️ Operation cancelled by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]❌ An error occurred: {str(e)}[/red]")
        sys.exit(1)
    finally:
        # Clean up: return to original directory and remove temp directory
        os.chdir(original_dir)
        if temp_dir and os.path.exists(temp_dir):
            try:
                shutil.rmtree(temp_dir, ignore_errors=True)
            except:
                pass

if __name__ == "__main__":
    init()  # Initialize colorama
    try:
        main()
    except Exception as e:
        console.print(f"\n[red]❌ An error occurred: {str(e)}[/red]")
        sys.exit(1)
