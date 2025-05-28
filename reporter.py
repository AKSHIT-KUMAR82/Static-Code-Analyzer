from colorama import Fore, Style

def print_banner(filepath):
    print(f"\n{Fore.CYAN}[+] Analyzing: {filepath}{Style.RESET_ALL}")
    print(f"{'-'*60}")

def print_issue(line_num, message, line):
    print(f"{Fore.RED}[Line {line_num}] {message}")
    print(f"    >> {line}{Style.RESET_ALL}")

def print_section(title, issues):
    print(f"\n{Fore.MAGENTA}{title}{Style.RESET_ALL}")
    if not issues:
        print(f"{Fore.GREEN}  None found.{Style.RESET_ALL}")
    else:
        for line_num, message, code_line in issues:
            print_issue(line_num, message, code_line)

def print_summary(count):
    if count == 0:
        print(f"{Fore.GREEN}No vulnerabilities or quality issues found.")
    else:
        print(f"\n{Fore.YELLOW}Total issues found: {count}{Style.RESET_ALL}")
