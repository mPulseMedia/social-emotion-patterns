# Environment Setup Documentation

## Overview
Documentation for environment configuration in the social-emotion-patterns project.

## Files

env_cursor	env/cursor.txt
Mirror of your Cursor user_rules settings in environment variable format. This file contains your development workflow preferences and coding standards.

.env	.env
Standard environment file for development variables (API keys, database connections, etc.). This file is git-ignored and contains sensitive configuration.

## User Rules Reference

The env_cursor file mirrors these Cursor user_rules:

- **format**: Response structure and documentation standards
- **prod_mgr**: Product management and tracking requirements  
- **name**: Naming conventions and terminology
- **prompt**: Chat formatting and audit requirements
- **dir**: Directory structure guidelines

## Usage

- Edit env_cursor to enable/disable specific user_rules
- Use `.env` for standard development environment variables
- Both files are excluded from git commits for security