import json
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RULES_DIR = BASE_DIR / "rules"
SOURCES_FILE = BASE_DIR / "sources.json"

RULES_DIR.mkdir(exist_ok=True)

def convert_line(line: str):
    line = line.strip()
    if not line or line.startswith("#"):
        return None

    if line.startswith("+."):
        return f"DOMAIN-SUFFIX,{line[2:]}"
    elif line.startswith("full:"):
        return f"DOMAIN,{line[5:]}"
    elif line.startswith("regexp:"):
        return f"DOMAIN-REGEX,{line[7:]}"
    elif line.startswith("keyword:"):
        return f"DOMAIN-KEYWORD,{line[8:]}"
    elif line.startswith("domain:"):
        return f"DOMAIN,{line[7:]}"
    else:
        return f"DOMAIN-SUFFIX,{line}"

def main():
    with open(SOURCES_FILE, "r", encoding="utf-8") as f:
        sources = json.load(f)

    for name, url in sources.items():
        print(f"Processing {name} ...")
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()

        lines = resp.text.splitlines()
        converted = []

        for line in lines:
            rule = convert_line(line)
            if rule:
                converted.append(rule)

        output_path = RULES_DIR / f"{name}.list"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(converted))

if __name__ == "__main__":
    main()
