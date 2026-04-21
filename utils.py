def get_color(text, type="info"):
    # Simple ANSI color codes
    colors = {
        "green": "\033[92m",
        "red": "\033[91m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "end": "\033[0m"
    }
    
    if type == "bad": return f"{colors['red']}{text}{colors['end']}"
    if type == "warn": return f"{colors['yellow']}{text}{colors['end']}"
    if type == "good": return f"{colors['green']}{text}{colors['end']}"
    return f"{colors['blue']}{text}{colors['end']}"

def get_score(issues, total_lines):
    if total_lines == 0: return 10
    # Penalty: 1.5 points off for every issue found
    score = 10 - (len(issues) * 1.5)
    return max(0, round(score, 1))