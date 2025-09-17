import sys
from checker import GitGouger

# ANSI escape codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"
def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <owner> <repo> [token]")
        sys.exit(1)

    owner, repo = sys.argv[1], sys.argv[2]
    token = sys.argv[3] if len(sys.argv) > 3 else None

    checker = GitGouger(owner, repo, token)
    results = checker.run_checks()
    counter = 0
    print(f"\nAudit for {owner}/{repo}:\n")
    for result in results:
        name = result["name"]
        status = result["status"]
        description = result ["description"]
        if "notes" in result:
            notes = result["notes"]
        else:
            notes = ""
        print(f"{BOLD + name + RESET}: {(GREEN + 'PASS' + RESET) if status else (RED + 'FAIL' + RESET)}")
        if status:
            counter += 1
        print(f"{BLUE}Description{RESET}: {description}\n{BLUE}Notes{RESET}: {notes} \n")
    if counter == len(results):
        FINAL = GREEN
    elif counter == 0:
        FINAL = RED
    else:
        FINAL = YELLOW
    print(f"{FINAL}{counter}/{len(results)} CHECKS PASSED{RESET}")

if __name__ == "__main__":
    main()
