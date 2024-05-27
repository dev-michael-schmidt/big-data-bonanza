import os
import tempfile
import zipfile
import tarfile

from abstracts import Archive
from constants import (XZ_SUFFIX, ZIP_SUFFIX)


class ZipHandler(Archive):
    SRC_FOLDER = os.getcwd()
    DEST_PATH = os.path.join(os.getcwd(), SRC_FOLDER)

    def __init__(self):
        super(ZipHandler, self).__init__()
        pass

    def extract(self, with_data=False):
        tempdir = tempfile.mkdtemp()
        with zipfile.ZipFile(f'{SRC_FOLDER}/{INCOMING_NAME}.{ZIP_SUFFIX}') as _zip:
            _zip.extractall(tempdir)

        if with_data:
            return tempdir

    def compress(self):
        tempdir = tempfile.mkdtemp()
        with tarfile.open(f'{DEST_PATH}/{DESTINATION_NAME}.{XZ_SUFFIX}', mode='w:xz') as _tar:
            _tar.add(tempdir)
            # TODO return the tar as file io??

    def transform(self):
        output = self.extract()
        result = self.compress()
        return result
