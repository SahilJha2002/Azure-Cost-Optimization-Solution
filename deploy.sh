#!/bin/bash
# deploy.sh - Simple example of Azure CLI commands

# Variables (change as needed)
RESOURCE_GROUP="billing-rg"
STORAGE_ACCOUNT="billingstorage$(date +%s)"
CONTAINER_NAME="archived-records"

az group create --name $RESOURCE_GROUP --location eastus

az storage account create     --name $STORAGE_ACCOUNT     --resource-group $RESOURCE_GROUP     --location eastus     --sku Standard_LRS

CONNECTION_STRING=$(az storage account show-connection-string --resource-group $RESOURCE_GROUP --name $STORAGE_ACCOUNT --query connectionString -o tsv)

az storage container create --name $CONTAINER_NAME --account-name $STORAGE_ACCOUNT --connection-string "$CONNECTION_STRING"