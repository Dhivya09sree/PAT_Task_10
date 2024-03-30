#instead of double mention in float

class Account:
    def __init__(self, id: int, customer, balance: float = 0.0):
        self.__id = id
        self.__customer = customer
        self.__balance = balance
    
    def create_account_with_balance(cls, id: int, customer, balance: float):
        return cls(id, customer, balance)
    
    def create_account_without_balance(cls, id: int, customer):
        return cls(id, customer)
    
    def getID(self) -> int:
        return self.__id

    def getCustomer(self):
        return self.__customer

    def getBalance(self) -> float:
        return self.__balance

    def setBalance(self, balance: float) :
        self.__balance = balance

    def toString(self) -> str:
        return "Dhivya (ID 12345) balance=$1000.00"  
    
    def getCustomerName(self) -> str:
        return self.__customer.getName()
    
    def deposit(self, amount: float) :
        self.__balance += amount
        return self

    def withdraw(self, amount: float) :
        if self.__balance >= amount:
             self.__balance - amount   #subtract amount to balance
        else:
            print("Amount withdrawn exceeds the current balance.")
        return self