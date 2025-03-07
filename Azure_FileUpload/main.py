from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

storage_account_key=''
storage_account_name=''
connection_string=''
container_name=''

def uploadToBlobStorage(file_path, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_container_client(container_name)

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)

    print("Uploaded"+file_name+"file to blob storage")

uploadToBlobStorage('C:/Users/username/Desktop/azure.jpg', 'azure.jpg')