import ast

def analyze_code(source):
    issues = []
    suggestions = []
    tree = ast.parse(source)
    lines = source.splitlines()

    for node in ast.walk(tree):
        # 1. Check Function Length
        if isinstance(node, ast.FunctionDef):
            func_len = len(node.body) # Counting main statements
            if func_len > 15: # Easier threshold
                issues.append(f"Function '{node.name}' is too long ({func_len} lines)")
                suggestions.append(f"Try breaking '{node.name}' into smaller pieces")

            # 2. Check for Bad Naming (short names)
            if len(node.name) < 3:
                issues.append(f"Function name '{node.name}' is too short")

        # 3. Check for Nested Loops
        if isinstance(node, ast.For):
            for child in node.body:
                if isinstance(child, (ast.For, ast.While)):
                    issues.append(f"Nested loop detected at line {node.lineno}")
                    suggestions.append("Nested loops can be slow. Check if you can optimize.")

        # 4. Check Variable Names
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            if len(node.id) < 2 and node.id not in ['i', 'j', 'k']:
                issues.append(f"Variable '{node.id}' is too short (line {node.lineno})")

    return issues, list(set(suggestions)) # set() removes duplicate suggestions