### Card Model
```json
{
  "card_id": "string",
  "card_number": "string (masked)",
  "card_type": "virtual|physical",
  "product_type": "reloadable|single_use",
  "provider": {
    "company": "greendot|go2bank|netspend|paypal|chime|serve|bluebird|accountnow|rushcard|moneycard|westernunion|hrblock|turbotax|brinks",
    "network": "visa|mastercard|amex|discover",
    "program_id": "string",
    "program_name": "string",
    "bin_range": "string"
  },
  "status": "created|dispatched|delivered|active|blocked|expired|closed",
  "balance": "number",
  "available_balance": "number",
  "currency": "string (ISO 4217)",
  "created_at": "datetime (ISO 8601)",
  "activated_at": "datetime (ISO 8601)",
  "expires_at": "datetime (ISO 8601)",
  "customer_id": "string",
  "activation": {
    "method": "online|phone|sms|mobile_app",
    "phone_number": "string",
    "website": "string",
    "required_info": ["array of required fields"]
  },
  "limits": {
    "daily_spend_limit": "number",
    "monthly_spend_limit": "number",
    "atm_withdrawal_limit": "number",
    "international_daily_limit": "number"
  },
  "features": {
    "international_usage": "boolean",
    "contactless_enabled": "boolean",
    "online_purchases": "boolean",
    "atm_access": "boolean",
    "mobile_check_deposit": "boolean",
    "bill_pay": "boolean",
    # Comprehensive Prepaid Card API Specification

## Table of Contents
1. [Overview](#overview)
2. [Authentication & Security](#authentication--security)
3. [API Endpoints](#api-endpoints)
4. [Data Models](#data-models)
5. [Error Handling](#error-handling)
6. [Rate Limiting](#rate-limiting)
7. [Webhooks](#webhooks)
8. [Compliance & Security](#compliance--security)
9. [Implementation Guidelines](#implementation-guidelines)

## Overview

### Base URL
```
Production: https://api.prepaidcards.com/v1
Sandbox: https://sandbox-api.prepaidcards.com/v1
```

### Supported Features
- Physical and virtual prepaid card management
- Real-time balance and transaction processing
- Multi-tier security with OAuth 2.0 and MFA
- Comprehensive fraud detection
- Webhook notifications
- Bulk operations support
- Advanced analytics and reporting

## Authentication & Security

### Authentication Methods

#### 1. OAuth 2.0 (Recommended)
```http
POST /auth/oauth/token
Content-Type: application/json

{
  "grant_type": "client_credentials",
  "client_id": "your_client_id",
  "client_secret": "your_client_secret",
  "scope": "cards:read cards:write transactions:read"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 3600,
  "scope": "cards:read cards:write transactions:read"
}
```

#### 2. API Key Authentication
```http
Authorization: Bearer your_api_key
X-API-Version: 1.0
X-Request-ID: unique_request_id
```

### Security Headers
All requests must include:
```http
Content-Type: application/json
X-Request-ID: unique_trace_id
X-Client-Version: 1.0.0
X-Timestamp: 2025-08-02T10:30:00Z
X-Signature: HMAC-SHA256_signature
```

### Multi-Factor Authentication
For sensitive operations, MFA is required:
```json
{
  "mfa_token": "123456",
  "mfa_method": "sms|email|totp"
}
```

## API Endpoints

### Supported Card Providers

Our API integrates with major prepaid card providers:

#### Network Partners
- **Visa**: Standard and premium prepaid cards
- **MasterCard**: Consumer and business prepaid solutions
- **American Express**: Serve and Bluebird prepaid cards
- **Discover**: Cashback and rewards prepaid cards

#### Major Prepaid Card Companies
- **GO2bank**: Mobile-first banking and prepaid cards
- **Green Dot**: Vanilla Visa/MasterCard prepaid cards
- **NetSpend**: Visa and MasterCard prepaid accounts
- **PayPal**: PayPal Prepaid MasterCard
- **Chime**: SpotMe and Credit Builder cards
- **Walmart MoneyCard**: Visa and MasterCard options
- **Serve (American Express)**: Traditional and mobile prepaid
- **Bluebird (American Express)**: No-fee prepaid debit
- **AccountNow**: Gold Visa and MasterCard prepaid
- **RushCard**: Live Unlimited and Select prepaid cards
- **Western Union**: NetSpend prepaid solutions
- **H&R Block**: Emerald prepaid MasterCard
- **TurboTax**: Refund transfer cards
- **Brinks**: Prepaid MasterCard solutions

### Card Management

#### Create Card
```http
POST /cards
Authorization: Bearer {token}
Content-Type: application/json
```

**Request:**
```json
{
  "card_type": "virtual|physical",
  "product_type": "reloadable|single_use",
  "provider": {
    "company": "greendot|go2bank|netspend|paypal|chime|serve|bluebird|accountnow|rushcard|moneycard|westernunion|hrblock|turbotax|brinks",
    "network": "visa|mastercard|amex|discover",
    "program_id": "prog_12345",
    "bin_range": "123456"
  },
  "initial_balance": 100.00,
  "currency": "USD",
  "customer": {
    "customer_id": "cust_12345",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "phone": "+1234567890",
    "ssn_last4": "1234",
    "date_of_birth": "1990-01-01",
    "address": {
      "street": "123 Main St",
      "city": "New York",
      "state": "NY",
      "zip": "10001",
      "country": "US"
    }
  },
  "design": {
    "template_id": "template_001",
    "custom_text": "Happy Birthday!",
    "logo_url": "https://example.com/logo.png",
    "brand_colors": {
      "primary": "#1a73e8",
      "secondary": "#34a853"
    }
  },
  "limits": {
    "daily_spend_limit": 500.00,
    "monthly_spend_limit": 2000.00,
    "atm_withdrawal_limit": 300.00,
    "international_daily_limit": 200.00
  },
  "features": {
    "international_usage": true,
    "contactless_enabled": true,
    "online_purchases": true,
    "atm_access": true,
    "mobile_check_deposit": true,
    "bill_pay": true,
    "direct_deposit": true
  }
}
```

**Response:**
```json
{
  "card_id": "card_abc123def456",
  "card_number": "****-****-****-1234",
  "card_type": "virtual",
  "product_type": "reloadable",
  "provider": {
    "company": "greendot",
    "network": "visa",
    "program_id": "prog_12345",
    "program_name": "Green Dot Visa Prepaid"
  },
  "status": "created",
  "balance": 100.00,
  "currency": "USD",
  "created_at": "2025-08-02T10:30:00Z",
  "expires_at": "2027-08-02T23:59:59Z",
  "customer_id": "cust_12345",
  "activation": {
    "method": "online|phone|sms",
    "phone_number": "1-866-795-7000",
    "website": "https://www.greendot.com/activate",
    "required_info": ["card_number", "security_code", "ssn_last4", "zip_code"]
  },
  "limits": {
    "daily_spend_limit": 500.00,
    "monthly_spend_limit": 2000.00,
    "atm_withdrawal_limit": 300.00,
    "international_daily_limit": 200.00
  },
  "features": {
    "international_usage": true,
    "contactless_enabled": true,
    "online_purchases": true,
    "atm_access": true,
    "mobile_check_deposit": true,
    "bill_pay": true,
    "direct_deposit": true,
    "routing_number": "124303162"
  }
}
```

#### Activate Card (Provider-Specific)
```http
POST /cards/{card_id}/activate
Authorization: Bearer {token}
```

**Request for Green Dot/Vanilla Cards:**
```json
{
  "activation_method": "online|phone|sms",
  "verification_data": {
    "ssn_last4": "1234",
    "zip_code": "10001",
    "date_of_birth": "1990-01-01",
    "security_code": "123"
  },
  "mfa_token": "654321",
  "device_info": {
    "device_id": "device_789",
    "ip_address": "192.168.1.1",
    "user_agent": "Mozilla/5.0..."
  }
}
```

**Request for GO2bank Cards:**
```json
{
  "activation_method": "mobile_app|online",
  "verification_data": {
    "phone_number": "+1234567890",
    "email": "user@example.com",
    "government_id": {
      "type": "drivers_license|state_id|passport",
      "number": "D123456789",
      "state": "NY"
    }
  },
  "digital_wallet_setup": {
    "apple_pay": true,
    "google_pay": true,
    "samsung_pay": false
  }
}
```

**Request for NetSpend Cards:**
```json
{
  "activation_method": "online|phone",
  "verification_data": {
    "ssn": "123456789",
    "employment_status": "employed|unemployed|student|retired",
    "income_source": "employment|benefits|other",
    "monthly_income": 3000.00
  },
  "account_preferences": {
    "overdraft_protection": true,
    "purchase_cushion": false,
    "alerts": {
      "sms": true,
      "email": true,
      "low_balance_threshold": 10.00
    }
  }
}
```

**Request for Chime Cards:**
```json
{
  "activation_method": "mobile_app",
  "verification_data": {
    "phone_verification": "654321",
    "email_verification": "abc123",
    "identity_verification": {
      "government_id_front": "doc_id_front_123",
      "government_id_back": "doc_id_back_456",
      "selfie": "selfie_doc_789"
    }
  },
  "account_setup": {
    "direct_deposit": {
      "employer_name": "ACME Corp",
      "routing_number": "103100195",
      "account_number": "auto_generated"
    },
    "spotme_enrollment": true,
    "credit_builder_interest": true
  }
}
```

**Request for PayPal Prepaid:**
```json
{
  "activation_method": "online|mobile_app",
  "verification_data": {
    "paypal_account": "user@example.com",
    "phone_number": "+1234567890",
    "ssn_last4": "1234"
  },
  "integration": {
    "link_paypal_account": true,
    "enable_paypal_transfers": true,
    "cashback_rewards": true
  }
}
```

#### Get Card Details
```http
GET /cards/{card_id}
Authorization: Bearer {token}
```

**Response:**
```json
{
  "card_id": "card_abc123def456",
  "card_number": "****-****-****-1234",
  "card_type": "virtual",
  "product_type": "reloadable",
  "status": "active",
  "balance": 87.50,
  "available_balance": 87.50,
  "currency": "USD",
  "created_at": "2025-08-02T10:30:00Z",
  "activated_at": "2025-08-02T11:00:00Z",
  "expires_at": "2027-08-02T23:59:59Z",
  "last_transaction_at": "2025-08-02T14:30:00Z",
  "customer_id": "cust_12345",
  "limits": {
    "daily_spend_limit": 500.00,
    "daily_spent": 12.50,
    "monthly_spend_limit": 2000.00,
    "monthly_spent": 12.50
  }
}
```

#### Update Card Status
```http
PATCH /cards/{card_id}/status
Authorization: Bearer {token}
```

**Request:**
```json
{
  "status": "blocked|active|suspended",
  "reason": "fraud_suspected|customer_request|expired",
  "notes": "Suspicious activity detected"
}
```

#### Bulk Card Operations
```http
POST /cards/bulk
Authorization: Bearer {token}
```

**Request:**
```json
{
  "operation": "create|activate|block",
  "cards": [
    {
      "card_type": "physical",
      "initial_balance": 50.00,
      "customer_id": "cust_001"
    },
    {
      "card_type": "virtual",
      "initial_balance": 100.00,
      "customer_id": "cust_002"
    }
  ]
}
```

### Balance & Transaction Management

#### Get Balance
```http
GET /cards/{card_id}/balance
Authorization: Bearer {token}
```

**Response:**
```json
{
  "card_id": "card_abc123def456",
  "balance": 87.50,
  "available_balance": 87.50,
  "pending_balance": 0.00,
  "currency": "USD",
  "last_updated": "2025-08-02T14:30:00Z"
}
```

#### Reload Card (Multi-Provider Support)
```http
POST /cards/{card_id}/reload
Authorization: Bearer {token}
```

**General Reload Request:**
```json
{
  "amount": 50.00,
  "currency": "USD",
  "reload_method": {
    "type": "bank_transfer|credit_card|debit_card|ach|cash|check|paypal|venmo|direct_deposit|tax_refund|employer_payroll",
    "provider_specific": {
      "green_dot": {
        "reload_locations": ["walmart", "cvs", "walgreens", "dollar_general"],
        "reload_pack_id": "pack_123456",
        "fee": 4.95
      },
      "netspend": {
        "reload_network": "netspend_reload_network",
        "location_id": "loc_789",
        "cashier_id": "cashier_001"
      },
      "chime": {
        "source": "linked_bank|mobile_check|cash_deposit",
        "bank_routing": "103100195",
        "bank_account": "acc_456789"
      },
      "paypal": {
        "paypal_account": "user@example.com",
        "funding_source": "paypal_balance|linked_bank|debit_card"
      },
      "go2bank": {
        "deposit_method": "mobile_check|ach_transfer|cash_deposit",
        "check_images": {
          "front": "check_front_img_123",
          "back": "check_back_img_456"
        }
      }
    }
  },
  "payment_source": {
    "type": "bank_account|credit_card|debit_card|cash",
    "source_id": "src_12345",
    "routing_number": "021000021",
    "account_number": "****1234",
    "verification_method": "micro_deposits|instant_verification"
  },
  "reference": "RELOAD_REF_001",
  "mfa_token": "123456",
  "location_data": {
    "store_id": "walmart_001",
    "address": "123 Main St, New York, NY",
    "cashier_id": "cashier_789"
  }
}
```

**Provider-Specific Reload Features:**

**Green Dot Reload Locations:**
```json
{
  "reload_locations": [
    {
      "retailer": "walmart",
      "fee": 3.00,
      "max_amount": 500.00,
      "availability": "24/7"
    },
    {
      "retailer": "cvs",
      "fee": 4.95,
      "max_amount": 500.00,
      "availability": "store_hours"
    },
    {
      "retailer": "walgreens",
      "fee": 5.95,
      "max_amount": 500.00,
      "availability": "store_hours"
    },
    {
      "retailer": "dollar_general",
      "fee": 4.95,
      "max_amount": 500.00,
      "availability": "store_hours"
    }
  ]
}
```

**NetSpend Reload Options:**
```json
{
  "reload_options": [
    {
      "method": "netspend_reload_network",
      "locations": 130000,
      "fee": 3.95,
      "max_amount": 500.00
    },
    {
      "method": "ach_transfer",
      "fee": 0.00,
      "max_amount": 5000.00,
      "processing_time": "1-3_business_days"
    },
    {
      "method": "direct_deposit",
      "fee": 0.00,
      "max_amount": 10000.00,
      "early_access": true
    }
  ]
}
```

**Chime Reload Methods:**
```json
{
  "reload_methods": [
    {
      "method": "mobile_check_deposit",
      "fee": 0.00,
      "max_amount": 5000.00,
      "processing_time": "instant",
      "daily_limit": 2000.00
    },
    {
      "method": "direct_deposit",
      "fee": 0.00,
      "early_access_days": 2,
      "max_amount": "unlimited"
    },
    {
      "method": "cash_deposit_partners",
      "partners": ["walgreens", "duane_reade"],
      "fee": 4.50,
      "max_amount": 1000.00
    }
  ]
}
```

**Response:**
```json
{
  "transaction_id": "txn_reload_789",
  "status": "pending|completed|failed",
  "amount": 50.00,
  "currency": "USD",
  "new_balance": 137.50,
  "created_at": "2025-08-02T15:00:00Z",
  "reference": "RELOAD_REF_001"
}
```

#### Process Transaction
```http
POST /transactions
Authorization: Bearer {token}
```

**Request:**
```json
{
  "card_id": "card_abc123def456",
  "amount": 25.99,
  "currency": "USD",
  "transaction_type": "purchase|withdrawal|refund",
  "merchant": {
    "name": "Coffee Shop",
    "category": "5814",
    "location": {
      "latitude": 40.7128,
      "longitude": -74.0060
    }
  },
  "pos_data": {
    "terminal_id": "term_001",
    "entry_mode": "chip|swipe|contactless|online"
  }
}
```

#### Get Transaction History
```http
GET /cards/{card_id}/transactions?limit=50&offset=0&from=2025-08-01&to=2025-08-02
Authorization: Bearer {token}
```

**Response:**
```json
{
  "transactions": [
    {
      "transaction_id": "txn_12345",
      "card_id": "card_abc123def456",
      "amount": -25.99,
      "currency": "USD",
      "transaction_type": "purchase",
      "status": "completed",
      "merchant": {
        "name": "Coffee Shop",
        "category": "5814",
        "mcc": "5814"
      },
      "created_at": "2025-08-02T14:30:00Z",
      "authorization_code": "AUTH123",
      "reference": "REF_001"
    }
  ],
  "pagination": {
    "total": 150,
    "limit": 50,
    "offset": 0,
    "has_more": true
  }
}
```

### User Management

#### Create Customer
```http
POST /customers
Authorization: Bearer {token}
```

**Request:**
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "phone": "+1234567890",
  "date_of_birth": "1990-01-01",
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "state": "NY",
    "zip": "10001",
    "country": "US"
  },
  "kyc_documents": [
    {
      "type": "drivers_license",
      "document_id": "doc_123",
      "verification_status": "verified"
    }
  ]
}
```

#### Update Customer
```http
PATCH /customers/{customer_id}
Authorization: Bearer {token}
```

### Analytics & Reporting

#### Get Card Analytics
```http
GET /analytics/cards?from=2025-08-01&to=2025-08-02&group_by=day
Authorization: Bearer {token}
```

**Response:**
```json
{
  "period": {
    "from": "2025-08-01",
    "to": "2025-08-02"
  },
  "metrics": {
    "cards_created": 150,
    "cards_activated": 142,
    "total_transactions": 1250,
    "total_volume": 45000.00,
    "average_transaction": 36.00
  },
  "breakdown": [
    {
      "date": "2025-08-01",
      "cards_created": 75,
      "transactions": 625,
      "volume": 22500.00
    }
  ]
}
```

### Fraud & Security

#### Report Suspicious Activity
```http
POST /security/reports
Authorization: Bearer {token}
```

**Request:**
```json
{
  "card_id": "card_abc123def456",
  "incident_type": "fraud_suspected|lost_card|stolen_card",
  "description": "Unusual spending pattern detected",
  "evidence": [
    {
      "type": "transaction_id",
      "value": "txn_suspicious_001"
    }
  ]
}
```

#### Get Security Alerts
```http
GET /security/alerts?status=open&severity=high
Authorization: Bearer {token}
```

## Data Models

### Card Model
```json
{
  "card_id": "string",
  "card_number": "string (masked)",
  "card_type": "virtual|physical",
  "product_type": "reloadable|single_use",
  "status": "created|dispatched|delivered|active|blocked|expired|closed",
  "balance": "number",
  "available_balance": "number",
  "currency": "string (ISO 4217)",
  "created_at": "datetime (ISO 8601)",
  "activated_at": "datetime (ISO 8601)",
  "expires_at": "datetime (ISO 8601)",
  "customer_id": "string",
  "limits": {
    "daily_spend_limit": "number",
    "monthly_spend_limit": "number",
    "atm_withdrawal_limit": "number"
  },
  "features": {
    "international_usage": "boolean",
    "contactless_enabled": "boolean",
    "online_purchases": "boolean"
  }
}
```

### Transaction Model
```json
{
  "transaction_id": "string",
  "card_id": "string",
  "amount": "number",
  "currency": "string (ISO 4217)",
  "transaction_type": "purchase|withdrawal|reload|refund|fee",
  "status": "pending|completed|failed|reversed",
  "merchant": {
    "name": "string",
    "category": "string",
    "mcc": "string"
  },
  "created_at": "datetime (ISO 8601)",
  "processed_at": "datetime (ISO 8601)",
  "authorization_code": "string",
  "reference": "string"
}
```

### Customer Model
```json
{
  "customer_id": "string",
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "phone": "string",
  "date_of_birth": "date",
  "address": {
    "street": "string",
    "city": "string",
    "state": "string",
    "zip": "string",
    "country": "string (ISO 3166-1)"
  },
  "kyc_status": "pending|verified|rejected",
  "risk_level": "low|medium|high",
  "created_at": "datetime (ISO 8601)"
}
```

## Error Handling

### Standard Error Response
```json
{
  "error": {
    "code": "INVALID_CARD_STATUS",
    "message": "Card must be in 'created' status to activate",
    "details": {
      "current_status": "blocked",
      "required_status": "created"
    },
    "request_id": "req_12345",
    "timestamp": "2025-08-02T10:30:00Z"
  }
}
```

### Error Codes
- `AUTHENTICATION_FAILED` (401)
- `INSUFFICIENT_PERMISSIONS` (403)
- `CARD_NOT_FOUND` (404)
- `INVALID_CARD_STATUS` (422)
- `INSUFFICIENT_BALANCE` (422)
- `TRANSACTION_DECLINED` (422)
- `RATE_LIMIT_EXCEEDED` (429)
- `INTERNAL_SERVER_ERROR` (500)

## Rate Limiting

### Rate Limits by Endpoint Type
- **Authentication**: 10 requests/minute
- **Card Operations**: 100 requests/minute
- **Balance Inquiries**: 200 requests/minute
- **Transaction Processing**: 50 requests/minute
- **Bulk Operations**: 5 requests/minute

### Rate Limit Headers
```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1627846261
X-RateLimit-Window: 60
```

## Webhooks

### Webhook Configuration
```http
POST /webhooks
Authorization: Bearer {token}
```

**Request:**
```json
{
  "url": "https://your-app.com/webhooks/prepaid-cards",
  "events": [
    "card.created",
    "card.activated",
    "card.blocked",
    "transaction.completed",
    "transaction.declined",
    "balance.low"
  ],
  "secret": "your_webhook_secret"
}
```

### Webhook Payload Example
```json
{
  "event_id": "evt_12345",
  "event_type": "card.activated",
  "created_at": "2025-08-02T11:00:00Z",
  "data": {
    "card_id": "card_abc123def456",
    "customer_id": "cust_12345",
    "status": "active",
    "activated_at": "2025-08-02T11:00:00Z"
  },
  "webhook_id": "wh_67890"
}
```

### Webhook Verification
```javascript
const crypto = require('crypto');

function verifyWebhook(payload, signature, secret) {
  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');
  
  return crypto.timingSafeEqual(
    Buffer.from(signature, 'hex'),
    Buffer.from(expectedSignature, 'hex')
  );
}
```

## Compliance & Security

### Security Measures
1. **Encryption**: AES-256 for data at rest, TLS 1.3 for data in transit
2. **PCI DSS**: Level 1 compliance for card data handling
3. **Data Tokenization**: Card numbers replaced with tokens
4. **Regular Security Audits**: Quarterly penetration testing
5. **Fraud Detection**: Real-time ML-based transaction monitoring

### Compliance Requirements
- **PCI DSS**: Payment Card Industry Data Security Standard
- **SOX**: Sarbanes-Oxley Act compliance
- **GDPR**: General Data Protection Regulation
- **CCPA**: California Consumer Privacy Act
- **SOC 2 Type II**: Service Organization Control 2

### Data Protection
```json
{
  "data_classification": "confidential",
  "encryption": {
    "algorithm": "AES-256-GCM",
    "key_management": "HSM-managed"
  },
  "retention_policy": {
    "transaction_data": "7_years",
    "customer_data": "5_years_after_last_activity",
    "audit_logs": "10_years"
  }
}
```

## Implementation Guidelines

### SDK Examples

#### Node.js SDK Usage
```javascript
const PrepaidCardAPI = require('@prepaid-api/node-sdk');

const client = new PrepaidCardAPI({
  apiKey: 'your_api_key',
  environment: 'production', // or 'sandbox'
  timeout: 30000
});

// Create a card
const card = await client.cards.create({
  card_type: 'virtual',
  product_type: 'reloadable',
  initial_balance: 100.00,
  currency: 'USD',
  customer: {
    customer_id: 'cust_12345',
    first_name: 'John',
    last_name: 'Doe',
    email: 'john.doe@example.com'
  }
});

// Process a reload
const reload = await client.cards.reload(card.card_id, {
  amount: 50.00,
  payment_method: {
    type: 'bank_transfer',
    source_id: 'src_12345'
  }
});
```

#### Python SDK Usage
```python
from prepaid_api import PrepaidCardClient

client = PrepaidCardClient(
    api_key='your_api_key',
    environment='production'
)

# Create a card
card = client.cards.create({
    'card_type': 'virtual',
    'product_type': 'reloadable',
    'initial_balance': 100.00,
    'currency': 'USD',
    'customer': {
        'customer_id': 'cust_12345',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com'
    }
})

# Get balance
balance = client.cards.get_balance(card['card_id'])
```

### Performance Considerations
- **Response Times**: < 200ms for balance inquiries, < 500ms for transactions
- **Throughput**: Support for 10,000+ TPS
- **Availability**: 99.9% uptime SLA
- **Global CDN**: Edge locations for reduced latency

### Monitoring & Observability
```json
{
  "metrics": {
    "response_time_p95": "150ms",
    "error_rate": "0.1%",
    "throughput": "5000_rps"
  },
  "alerts": {
    "high_error_rate": "> 1%",
    "slow_response": "> 1000ms",
    "service_down": "availability < 99%"
  }
}
```

### Testing
- **Unit Tests**: 95%+ code coverage
- **Integration Tests**: End-to-end API testing
- **Load Testing**: Peak capacity validation
- **Security Testing**: Regular penetration testing
- **Chaos Engineering**: Resilience testing

This comprehensive API specification provides a robust foundation for prepaid card management with enterprise-grade security, compliance, and scalability features.
