# Solana Token Custody Analyzer

A Python-based tool for analyzing Solana tokens, supporting both standard SPL tokens and Token-2022 program tokens, with special verification for Pump.Fun tokens.

## Features

### Token Analysis
- **Program Verification**:
  - Standard SPL Token Program
  - Token-2022 Program
- **Metadata Retrieval**:
  - Token name and symbol
  - Update authority
  - Program ownership

### Security Features Detection
- **Standard SPL Tokens**:
  - Freeze authority status
- **Token-2022 Program Extensions**:
  - Permanent delegate
  - Transaction fees
  - Transfer hook programming
  - Confidential transfers
  - Token metadata

### Pump.Fun Token Verification
- **Authority Verification**:
  - Update authority check against Pump.Fun authority
- **Program Interaction**:
  - Verification of Pump.Fun program interaction
  - Raydium AMM program interaction detection
- **Token Status**:
  - Genuine Pump.Fun token verification
  - Raydium graduation status using Raydium API https://api-v3.raydium.io/docs/
  - Transaction signature tracking
  - Interacting account details

### Processing Capabilities
- Single token analysis
- Concurrent batch processing
- Rate-limiting and retry logic
- Exponential backoff for API calls

## Technical Details

### Dependencies
- Python 3.8+
- aiohttp: For async HTTP requests
- solders: For Solana public key operations
- logging: For detailed operation logging

### Configuration
- Customizable RPC endpoint
- Adjustable rate limits
- Configurable retry parameters
- Concurrent processing limits

## Usage

### Command Line Interface

#### Single Token Analysis
```bash
# Basic usage
python token_report_cli.py <token_address>

# With custom output directory
python token_report_cli.py <token_address> --output ./reports

# Example
python token_report_cli.py Hb3vHHZFpnQ61sCQF4myZm8QsYVYng3ULXu9zDTxpump
```

#### Batch Processing
```bash
# Basic batch processing
python token_report_cli.py <input_file.txt> --batch

# With custom output directory
python token_report_cli.py <input_file.txt> --batch --output ./reports

# Example
python token_report_cli.py spl-addresses-test.txt --batch
```

### Input File Format
The input file for batch processing should contain one token address per line:
```text
Hb3vHHZFpnQ61sCQF4myZm8QsYVYng3ULXu9zDTxpump
DZABY9tvW2yj6qmgYTJdigeWUBNVEcXTawJyAigupump
BS9ecLr44AkZBa8udScJUgiYnGMH6swojZWyQorkpump
...
```

### Output Files
- **PDF Reports**: Individual security assessment reports for each token
  - Format: `{token_name} ({token_symbol}) Security Memo.pdf`
  - Location: Current directory or specified output directory
- **JSON Results** (Batch Processing):
  - Format: `batch_results_YYYYMMDD_HHMMSS.json`
  - Contains detailed analysis for all processed tokens
- **Log File**:
  - Format: `batch_results_YYYYMMDD_HHMMSS.log`
  - Contains processing details and error messages

### Example Output Structure
```json
{
  "name": "Token Name",
  "symbol": "SYMBOL",
  "address": "token_address",
  "owner_program": "Token Program",
  "freeze_authority": null,
  "update_authority": "authority_address",
  "security_review": "PASSED/FAILED",
  "is_genuine_pump_fun_token": true/false,
  "token_graduated_to_raydium": true/false
}
```

## Security Review Criteria

### Standard SPL Tokens
- PASSED: No freeze authority
- FAILED: Has freeze authority

### Token-2022 Program
- PASSED: No security-sensitive features
- FAILED: Has any of:
  - Freeze authority
  - Permanent delegate
  - Transfer hook
  - Confidential transfers
  - Non-zero transfer fees

### Pump.Fun Verification
- Checks update authority
- Verifies program interactions
- Tracks Raydium graduation status

## Error Handling
- Robust retry mechanism
- Rate limit handling
- Detailed error logging
- Graceful failure recovery
