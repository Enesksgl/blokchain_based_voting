import hashlib
import datetime


class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):  # TODO Özet fonksiyonu ekle
        sha = hashlib.sha256()
        hash_str = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

    def toJson(self):
        return {
            'timestamp': str(self.timestamp),
            'data': str(self.data),
            'previousHash': str(self.previous_hash),
            'hash': str(self.hash)
        }


class Blockchain:
    chain = []

    def __init__(self):
        print("init")
        self.chain.append(Block("Genesis Block", 0))

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(data, previous_block.hash)
        self.chain.append(new_block)

    def getLastBlock(self):
        return self.chain[len(self.chain)-1]
