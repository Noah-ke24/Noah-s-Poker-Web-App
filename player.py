#inheritance
import random
import time

class Player():

    def __init__(self, type="pc", cards=[], total_amount_bet=0, name="", amount=0):
        self.name=name
        self.type=type
        self.cards=cards
        self.total_amount_bet=total_amount_bet
        self.amount=amount

    def place_initial_bet(self):
        while True:
            amount=input("Place initial bet amount.Current amount is {self.amount}: ")
            if amount.isdigit():
                n=int(amount)
                if n>0 and n<=self.amount:
                    self.amount=self.amount-n #use a setter
                    return n
                print("Invalid amount entered.")
                print("amount must range from 1 to {self.amount}")
                print("try again")

            else:
                print("enter a number as valid amount between 1 and {self.amount}")

    def call_fold_raise(self, player):
        choice=input("Press 1 to call \nPress 2 fold \nPress 3 to raise ")
        if choice== "1":
            return self.call(player)
        if choice=="2":
            return self.fold(player)
        if choice=="3":
            return self.raise_stake(player)
        print("wrong choice {choice}. choose 1 to 3")
        self.call_fold_raise(player)

    def call(self, player):
        print("call action")

    def fold(self, player):
        print("Fold")
        return "l"

    def raise_stake(self, player):
        print("raise amount")

    def auto_match_or_raise(self, amount):
        print("I'M thinking.What to do")
        time.sleep(2)
        to_do=random.randint(1,2)
        raise_amount=random.randint(10,250)

        if raise_amount>self.amount:
            to_do=1
        if to_do==1:
            if self.amount>amount:
                self.amount=self.amount-amount
                print(f"Matching your action. Bet {amount}")
                return amount
            else:
                return "l"

        self.amount=self.amount-raise_amount
        print("I have a good feeling. I raise by ",raise_amount)
        return raise_amount

    def update_amount_bet(self, amount):
        self.total_amount_bet=self.total_amount_bet+amount

    def reset_amount_bet(self):
        self.total_amount_bet=0
