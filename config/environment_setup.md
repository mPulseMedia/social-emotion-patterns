# User Rules Environment Setup

## Overview
Mirror of Cursor settings user_rules in environment variable format.

## Quick Start
```bash
cp environment_template.env .env
```

## User Rules Variables

### user_rule format
- `USER_RULE_FORMAT_ENABLED`: Enable format rules
- Rules: name and short description, longer subpoints, requirements/testcase/documentation

### user_rule prod_mgr  
- `USER_RULE_PROD_MGR_ENABLED`: Enable product management rules
- Rules: maintain requirement, testcase, status, documentation, crossreference, index files

### user_rule name
- `USER_RULE_NAME_ENABLED`: Enable naming conventions
- Rules: snake_case terms, root concept first, singular forms, consistent terminology

### user_rule prompt
- `USER_RULE_PROMPT_ENABLED`: Enable prompt formatting
- Rules: header format, nested bullets, user_rule audit confirmation

### user_rule dir
- `USER_RULE_DIR_ENABLED`: Enable directory rules  
- Rules: keep simple and minimal

## Usage
Set variables to `true`/`false` to enable/disable specific rule sets in your development workflow.
