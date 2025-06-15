# Azure Cost Optimization: Billing Record Archival

## Problem Statement
Billing records are stored in Azure Cosmos DB. The system is read-heavy, but records older than 3 months are rarely accessed. Cosmos DB costs are rising due to increased data size.

## Solution Summary
Offload records older than 3 months to Azure Blob Storage. Modify the API layer to serve requests from either Cosmos DB or Blob, based on record age. No API contract changes required.

## Architecture Diagram
See `architecture.mmd` for Mermaid diagram.

## Components Used
- Azure Cosmos DB
- Azure Blob Storage
- Azure Functions (Python)
- Azure Logic Apps / Durable Functions
- Metadata store (Cosmos DB or Azure Table)
- Python Scripts for Archival and API logic

## Files
- `archive.py`: Archive old records to Blob Storage.
- `api_layer.py`: API read logic to fetch data from appropriate store.
- `architecture.mmd`: Mermaid.js diagram of solution.
- `deploy.sh`: Azure CLI deployment script.

## Requirements
- Azure Subscription
- Python 3.x
- Azure CLI

## Deployment
```bash
az login
./deploy.sh
```

## License
MIT
