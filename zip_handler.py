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
        pass
    def extract(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            with zipfile.ZipFile(f'{SRC_FOLDER}/{INCOMING_NAME}.{ZIP_SUFFIX}') as _zip:
                _zip.extractall(tmpdir)

    def compress(self):
        with tarfile.open(f'{DEST_PATH}/{DESTINATION_NAME}.{XZ_SUFFIX}', mode='w:xz') as _tar:
            _tar.add(tmpdir)
