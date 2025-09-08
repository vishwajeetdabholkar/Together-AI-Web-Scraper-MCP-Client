# Test Suite

This directory contains the test suite for AI Web Scraper Pro.

## Structure

- `unit/` - Unit tests for individual components
- `integration/` - Integration tests for API endpoints
- `fixtures/` - Test data and fixtures

## Running Tests

### All Tests
```bash
pytest tests/
```

### Unit Tests Only
```bash
pytest tests/unit/
```

### Integration Tests Only
```bash
pytest tests/integration/
```

### With Coverage
```bash
pytest tests/ --cov=backend --cov-report=html
```

## Test Categories

### Unit Tests
- Test individual functions and classes
- Mock external dependencies
- Fast execution
- Isolated testing

### Integration Tests
- Test API endpoints
- Test component interactions
- Use real dependencies where possible
- End-to-end scenarios

## Writing Tests

### Unit Test Example
```python
import pytest
from unittest.mock import Mock, patch
from backend.mcp_client import MCPWebScraperClient

def test_mcp_client_initialization():
    client = MCPWebScraperClient()
    assert client.server_command == "python"
    assert client.server_path is not None
```

### Integration Test Example
```python
import pytest
import requests

def test_health_endpoint():
    response = requests.get("http://localhost:9000/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
```

## Test Configuration

Tests use pytest configuration from `pyproject.toml`:
- Coverage reporting
- Test discovery patterns
- Output formatting

## Fixtures

Common test fixtures are available in `fixtures/`:
- Sample web pages
- Mock API responses
- Test data sets
