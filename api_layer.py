# api_layer.py
# API logic to fetch data from Cosmos DB or Blob depending on archival status

import json
from azure.storage.blob import BlobServiceClient

def get_record(record_id):
    record = cosmos.get_item(record_id)
    if not record.get("archived", False):
        return record
    else:
        blob_client = blob_service.get_blob_client(container="archived-records", blob=record['id'] + ".json")
        blob_data = blob_client.download_blob().readall()
        return json.loads(blob_data)