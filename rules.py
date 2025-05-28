def detect_gets(line):
    if "gets(" in line:
        return "Unsafe function (possible buffer overflow)"

def detect_strcpy(line):
    if "strcpy(" in line or "strcat(" in line:
        return "Unsafe function (possible buffer overflow / injection)"

def detect_hardcoded_password(line):
    if 'password' in line and '"' in line:
        return "Hardcoded password found"


def detect_redundant_code(line):
   
    if line.strip() == "":
        return "Redundant empty line"
    if line.strip().startswith("// TODO") or line.strip().startswith("// FIXME"):
        return "Reminder comment present (consider cleaning before production)"


def detect_unused_variables(line):
    if ("int " in line or "char " in line or "float " in line) and ";" in line and "=" not in line:
        return "Possible unused variable declaration"
