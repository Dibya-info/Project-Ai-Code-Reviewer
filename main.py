import sys
from utils import get_color, get_score
from analyzer import analyze_code

def main():
    print(get_color("=== AI CODE REVIEWER CLI ===", "good"))
    print("1. Paste Code\n2. Open .py File")
    
    choice = input("\nChoose option: ")
    code = ""

    if choice == '1':
        
        print("\nPaste code (Press ENTER twice to finish):")
        lines = []
        while True:
            try:
                line = input()
                if line == "": break
                lines.append(line)
            except EOFError:
                break
        code = "\n".join(lines)
        
    elif choice == '2':
        filename = input("Enter filename: ")
        try:
            with open(filename, 'r') as f:
                code = f.read()
        except FileNotFoundError:
            print(get_color("File not found!", "bad"))
            return

    if not code.strip():
        print("No code provided.")
        return

    
    try:
        issues, suggestions = analyze_code(code)
        score = get_score(issues, len(code.splitlines()))
        print(f"\nCODE QUALITY SCORE: {get_color(str(score) + '/10', 'good' if score > 7 else 'bad')}")
        
        for msg in issues:
            print(f" • {msg}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()