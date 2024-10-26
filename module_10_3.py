from threading import *
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        self.lock.acquire()

    def deposit(self):
        for i in range(100):
            dep = randint(50, 500)
            if self.balance <= 500 and self.lock.locked():
                self.lock.release()
                self.balance += dep
                print(f'Пополнение: {dep}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            dep = randint(50, 500)
            print(f'Запрос на {dep}')
            if dep <= self.balance:
                self.balance -= dep
                print(f'Снятие: {dep}. Баланс: {self.balance}')
            elif dep > self.balance:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
