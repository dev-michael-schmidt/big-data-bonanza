from abc import ABC, abstractmethod

class Archive(ABC):

    def __init__(self):
        pass

    def extract(self):
        pass

    def compress(self):
        pass

    def __iter__(self):
        pass  # iterate through objects in archive
