# metacubex_clash-shadowrocket
# MetaCubeX Clash → Shadowrocket Rule Converter

Repository name: metacubex_clash-shadowrocket

This project automatically converts MetaCubeX geosite/geoip rule lists into Shadowrocket-compatible rule sets and keeps them updated via GitHub Actions.

## Features

- Supports geosite and geoip rule sources from MetaCubeX
- Converts to Shadowrocket formats:
  - DOMAIN
  - DOMAIN-SUFFIX
  - DOMAIN-KEYWORD
  - DOMAIN-REGEX
- Auto-updates every 6 hours
- Ready-to-use raw links for Shadowrocket rule-set import

## Directory Structure

- `sources.json`: Source rule list URLs
- `scripts/convert.py`: Conversion engine
- `rules/`: Output Shadowrocket rule files
- `.github/workflows/update.yml`: Auto-update workflow

## Example Usage (Shadowrocket)

Import rule set using raw GitHub link:

https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/metacubex_clash-shadowrocket/main/rules/openai.list

## Update Schedule

Every 6 hours or manually via GitHub Actions UI.
