from azure.storage.blob import BlobClient, ResourceTypes


import constants as c

class BlobWorker(BlobClient):

    def __init__(self, name, data=None):

        self.container_name = c.CONTAINER_NAME
        self.blob_name = c.BLOB_NAME

        self.credentials = c.CREDENTIALS
        self.account_url = c.ACCOUNT_URL

        self.data = data
        super().__init__(self.account_url,
                         self.credentials,
                         self.blob_name)

        self.resource_types = ResourceTypes(service=True)
        self.resource = 'file'


    def push(self):

        if self.data:
            self.upload_blob(self.data)

    def pop(self):

        data = self.peek()
        self.delete_blob()
        return data

    def peek(self):

        data = self.download_blob()
        return data


def main():

    # TODO open a file instead of 'foo'
    worker = BlobWorker('__main__', b'foo')


if __name__ == "__main__":
    try:
        main()
        pass
    except Exception as e:
        print(e)

    print("we've reached the end")
