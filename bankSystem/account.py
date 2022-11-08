import bankSystem
import random

from bankSystem.transactions import trasactionsDef


class Account():
    accountID = 0
    userID:str
    balance = 0

    def __int__(self, userID, balance):
        accountID = random.getrandbits(32)
        self.userID = userID
        self.balance = balance

    def withDraw(self, valor):
        if (valor > self.balance):
            print("Saldo insuficiente")
        elif(valor <= self.balance):
            self.balance = self.balance - valor
            print("Saque realizado com sucesso!\n")

    def deposit(self, valor):
        self.balance = self.balance + valor
        print("Deposito realizado com sucesso")

    def available(self):
        print("------ BANK ----------------------")
        print("----------------------------------")
        print("ID da conta: "+ self.accountID)
        print("ID do Usuario: "+ self.userID)
        print("Saldo: "+ self.balance)
        print("----------------------------------")

    def transactions(self):
        trasactionsDef()