import sys
from utils import read_code
from rule_registry import RULES
from reporter import print_banner, print_section, print_summary
from constants import BANNER

def analyze_code(filepath):
    print(BANNER)
    lines = read_code(filepath)
    if not lines:
        return

    print_banner(filepath)

    security_issues = []
    quality_issues = []

    for i, line in enumerate(lines, start=1):
        for category, rule in RULES:
            result = rule(line)
            if result:
                issue = (i, result, line.strip())
                if category == "Security":
                    security_issues.append(issue)
                elif category == "Quality":
                    quality_issues.append(issue)

    # Print issues with sections
    print_section("🔒 Security Issues:", security_issues)
    print_section("🛠️ Code Quality Suggestions:", quality_issues)

    total_issues = len(security_issues) + len(quality_issues)
    print_summary(total_issues)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python codeguardian.py <source_file.c>")
    else:
        analyze_code(sys.argv[1])
