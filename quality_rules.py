def detect_redundant_true_check(line):
    if '== True' in line or '== False' in line:
        return "Redundant boolean comparison (use condition directly)"

def detect_magic_numbers(line):
    import re
    # Skip if it's part of common functions like printf or scanf
    if re.search(r'\b\d+\b', line) and not any(func in line for func in ['printf', 'scanf']):
        return "Possible magic number used (consider using a named constant)"

def detect_empty_if_block(line):
    if 'if' in line and '{' in line and '}' in line and line.strip().endswith('{}'):
        return "Empty 'if' block (redundant or placeholder)"

def detect_redundant_assignment(line):
    if ' = ' in line and line.strip().split('=')[0].strip() in line.strip().split('=')[1]:
        return "Redundant self-assignment detected"
