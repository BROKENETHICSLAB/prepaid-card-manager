"""
Configuration settings for the prepaid card manager
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Configuration files
CONFIG_FILE = os.path.expanduser("~/.prepaid_config.json")
DATABASE_FILE = os.path.expanduser("~/.prepaid_store.db")
LOG_FILE = os.path.expanduser("~/.prepaid_logs.txt")

# API Settings
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
RATE_LIMIT_DELAY = 1.0

# Database settings
DB_POOL_SIZE = 5
DB_TIMEOUT = 30

# Security settings
TOKEN_BUFFER_TIME = 300  # 5 minutes before expiry
MAX_SESSION_TIME = 3600  # 1 hour

# Limits
MAX_RELOAD_AMOUNT = 500.00
MIN_RELOAD_AMOUNT = 1.00
MAX_DAILY_TRANSACTIONS = 100

# Receipt settings
RECEIPT_WIDTH = 40
RECEIPT_FONT_SIZE = 12

# Logging
LOG_LEVEL = "INFO"
LOG_MAX_SIZE = 10 * 1024 * 1024  # 10MB
LOG_BACKUP_COUNT = 5

# Provider settings
PROVIDER_CONFIG_FILE = BASE_DIR / "config" / "providers.json"
