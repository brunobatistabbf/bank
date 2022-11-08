import bankSystem
import random



class Account():
    accountID = 0
    userID:str
    balance = 0
    transacoes = 0

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
            self.transacoes = self.transacoes + 1

    def deposit(self, valor):
        self.balance = self.balance + valor
        print("Deposito realizado com sucesso")
        self.transacoes = self.transacoes + 1

    def available(self):
        print("------ BANK ----------------------")
        print("----------------------------------")
        print("ID da conta: "+ self.accountID)
        print("ID do Usuario: "+ self.userID)
        print("Saldo: "+ self.balance)
        print("Numero de transacoes: " + self.transacoes)
        print("----------------------------------")

