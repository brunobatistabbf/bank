import random
from typing import Type, Any


class client():
    userID = 0
    name:str
    CPF:int
    cellphone:int
    email:str
    adress:str

    def __int__(self, name, cpf, cellphone, email, adress):
        self.name = name
        self.CPF = cpf
        self.cellphone = cellphone
        self.email = email
        self.adress = adress
        self.userID = random.getrandbits(32)

    def dadosClient(self, name):
        if(name == self.name):
            print("ID do usuario: " + self.userID)
            print("Nome: "+ self.name)
            print("Telefone: " + self.cellphone)
            print("Email: "+ self.email)
            print("Endereço: "+ self.adress)

    