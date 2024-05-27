import io

from azure.storage.blob import BlobClient, ResourceTypes
from azure.storage.blob import BlobServiceClient

import constants as c


class BlobClientWorker:

    def __init__(self, account_url, credentials, container_name, blob_name, blob_data):
        self.container_name = container_name
        self.blob_name = blob_name

        self.credentials = credentials
        self.account_url = account_url

        self.blob_data = blob_data

        self.client = BlobServiceClient(account_url, credentials).get_blob_client(self.container_name, blob_name)

    def push(self):
        if self.blob_data:
            self.client.upload_blob(self.blob_data)

    def pull(self):
        if self.client.exists():
            return self.client.download_blob()

    def pop(self):
        if self.client.exists():
            data = self.client.download_blob()
            self.client.delete_blob()
            return data


def main():
    # TODO open a file instead of 'foo'
    fh = open('sample_data.txt', 'rb')
    worker = BlobClientWorker(c.ACCOUNT_URL, c.CREDENTIALS, c.CONTAINER_NAME, c.BLOB_NAME, fh)
    data = worker.pull()
    pass


if __name__ == "__main__":
    try:
        main()
        pass
    except Exception as e:
        print(e)

    print("we've reached the end")
