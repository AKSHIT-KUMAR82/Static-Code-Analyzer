from rules import detect_gets, detect_strcpy, detect_hardcoded_password, detect_redundant_code, detect_unused_variables

# Now each rule is paired with its category: "Security" or "Quality"
RULES = [
    ("Security", detect_gets),
    ("Security", detect_strcpy),
    ("Security", detect_hardcoded_password),
    ("Quality", detect_redundant_code),
    ("Quality", detect_unused_variables),
]
