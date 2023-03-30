import hashlib
import datetime
import json


class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

    def toJson(self):
        return {
            'timestamp': self.timestamp,
            'data': self.data,
            'previousHash': self.previous_hash,
            'hash': self.hash
        }


class Blockchain:
    chain = []

    def __init__(self):
        print("init")
        self.chain.append(Block("Genesis Block", "0").toJson())

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(data, previous_block.hash)
        self.chain.append(new_block)

    def getLastBlock(self):
        return self.chain[len(self.chain)-1]
class User:
    def __init__(self, id,username,password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return f"User ID: {self.id}, Username: {self.username}"
    
class Login:
    def __init__(self, users):
        self.users = users
        self.logged_in_user = None

    def authenticate(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.logged_in_user = user
                return True
            return False
    def logout(self):
        self.logged_in_user = None

# örnek kullanıcılar
users = [
    User(1, "Muhammet Ali", "Muhammet123"),
    User(2, "Enes", "Enes123"),
]

login = Login(users)
username = input("Kullanici adi:")
password = input("Şifre: ")
if login.authenticate(username, password):
    print(f"{login.logged_in_user.username} başariyla giris yapti" )
    #kullanıcı ile ilgili işlemlerin yapılacağı kısım..
    login.logout()

else:
    print("Kullanici adi veya şifre hatali")


class Election:
    def __init__(self, id, name, candidates, date, participants):
        self.id = id
        self.name = name
        self.candidates = candidates
        self.date = date
        self.participants = participants
        self.previous_hash = None
        self.hash = self.calculate_hash()

    def calculate_hash(self):
       
       "Election(Seçim) instance'in SHA-256 hash değerini hesaplayan kisim" 

       hash_string = str(self.id) + self.name + str(self.date) + str(self.candidates) + str(self.participants)
       if self.previous_hash:
           hash_string += self.previous_hash
       return hashlib.sha256(hash_string.encode()).hexdigest()
    
    def add_to_blokchain(self, blokchain):
        """
        Election instance'ini blokchaine ekleyen kisim
        """
        if blokchain:
            self.previous_hash = blokchain[-i].hash
        blokchain.append(self)

    def __str__(self):
        return f"Election ID: {self.id}, Name {self.name}, Date: {self.date}"
    
# Örnek kullanım

user1 = User(1, "Muhammet Ali")
user2 = User(2, "Enes")
users = [user1, user2]

election1 = Election(1, "Başkanlık Seçimi", ["Recep Tayyip Erdoğan"], datetime.datetime.now(), users)

blockchain = []
election1.add_to_blokchain(blockchain)

for block in blockchain:
    print(block)
