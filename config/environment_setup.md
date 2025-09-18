# Environment Setup Guide

## Overview
This guide explains how to set up environment variables for the social-emotion-patterns project.

## Quick Start

1. **Copy the template:**
   ```bash
   cp environment_template.env .env
   ```

2. **Fill in your values:**
   Edit `.env` with your actual API keys and configuration

3. **Verify setup:**
   Your `.env` file should never be committed to git (it's in `.gitignore`)

## Environment Variables

### Application Settings
- `APP_NAME`: Project identifier
- `NODE_ENV`: Environment (development/production/test)
- `PORT`: Server port (default: 3000)

### Database Configuration
- `DATABASE_URL`: Full PostgreSQL connection string
- `DB_HOST`, `DB_PORT`, `DB_NAME`: Individual database settings
- `DB_USER`, `DB_PASSWORD`: Database credentials

### API Keys Required
- `OPENAI_API_KEY`: For AI-powered emotion analysis
- `ANTHROPIC_API_KEY`: Alternative AI provider
- `GOOGLE_API_KEY`: For various Google services

### Social Media APIs
- `TWITTER_API_KEY`, `TWITTER_API_SECRET`: Twitter API access
- `FACEBOOK_ACCESS_TOKEN`: Facebook Graph API
- `INSTAGRAM_ACCESS_TOKEN`: Instagram Basic Display API

### Security
- `JWT_SECRET`: For token generation (use strong random string)
- `SESSION_SECRET`: For session management

### External Services
- `REDIS_URL`: For caching and queues
- `ELASTICSEARCH_URL`: For search functionality
- `AWS_*`: For cloud storage and services

### Email Configuration
- `SMTP_*`: For sending emails
- `FROM_EMAIL`: Default sender address

### Monitoring
- `GOOGLE_ANALYTICS_ID`: For web analytics
- `SENTRY_DSN`: For error tracking
- `LOG_LEVEL`: Logging verbosity

### Feature Flags
- `ENABLE_EMOTION_ANALYSIS`: Toggle emotion processing
- `ENABLE_SOCIAL_MONITORING`: Toggle social media monitoring
- `ENABLE_REAL_TIME_PROCESSING`: Toggle real-time features

## Security Best Practices

1. **Never commit `.env` files**
2. **Use strong secrets** (generate with `openssl rand -hex 32`)
3. **Rotate keys regularly**
4. **Use different values** for development/production
5. **Limit API key permissions** to minimum required

## Environment-Specific Files

- `.env` - Your local development environment
- `.env.production` - Production environment (deploy separately)
- `.env.test` - Testing environment
- `environment_template.env` - Template for new developers

## Troubleshooting

### Common Issues
- **Missing variables**: Check template for required keys
- **Connection errors**: Verify database/service URLs
- **Permission errors**: Check API key scopes and limits

### Validation
Create a simple validation script to check your environment:
```bash
node -e "console.log('Environment loaded:', !!process.env.DATABASE_URL)"
```
