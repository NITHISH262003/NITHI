

class TrainBooking:
    def __init__(self, total_seats):
        self.seats = {} 
        for seat in range(1, total_seats + 1):
            self.seats[seat] = "Available" 
        # print(self.seats)


    def book_seat(self, seat_number):
        if seat_number in self.seats and self.seats[seat_number] == "Available":
            self.seats[seat_number] = "Reserved"
            print( "successfully booked!")
            # print(self.seats)
        else:
            print(f"Seat {seat_number} is already reserved or does not exist.")

    def check_seat_status(self, seat_number):
        if seat_number in self.seats:
            print(f"Seat {seat_number} is {self.seats[seat_number]}.")
        else:
            print("Invalid seat number.")

train = TrainBooking(total_seats=10)

# train.book_seat(5)
# train.check_seat_status(5)
# train.check_seat_status(8) 

class PriceCompere:
    def __init__(self):
        self.products={}

    def add_store(self,name,store,price):
        if name not in self.products:
            self.products[name]=[]
            self.products[name].append((store,price))
        # print(self.products)

    def lowest_price(self,name):
        if name in self.products:
            min_store,min_price=None,float('inf')
            for store,price in self.products[name]:
                if price<min_price:
                    min_price=price
                    min_store=store
            print(f"Lowest price for{name}:?{min_price} at {min_store}")
        else:
            print(f'{name} not found')
        
    def search_product(self, name):
            if name in self.products:
                print(f"Prices for {name}:")
                for store, price in self.products[name]:
                    print(f"- {store}: ₹{price}")
            else:
                print(f"{name} not found.")
                    
# shop=PriceCompere()
# shop.add_store('laptop','dell',20000)
# shop.add_store('laptop','hp',10000)
# shop.add_store('laptop','lenova',50000)
# shop.add_store('laptop','apple',23400)
# shop.add_store('phone','apple',23400)
# shop.add_store('phone','apple',23400)
# shop.lowest_price('laptop')
# shop.search_product('phone')



class KotakBank:
    location="salem"
    ceo="Nithishs"
    isfc_code="420JKAHSDLBVFK"
    def __init__(self,name:str,account_no:int,pin:int,balance:int):
        self.name=name
        self.balance = balance
        self._account_no = account_no
        self.__pin = pin
        self.transaction = []
    def deposit(self,amount:int):
        print(f"depositing rs.{amount} into your account")
        self.balance+=amount
        self.transaction.append(f"deposited rs.{amount}")
        # print(self.transaction)
    def withdraw(self,pin:int,amount:int):
        if self.__pin == pin:
            if self.balance>amount:
                print(f"{amount}debited")
                self.balance-=amount
                self.transaction.append(f"{amount}debited")
                # print(self.transaction)
            else:
                print("Insufficent balance")
        else:
            print("Wrong pin")
    def display_transactions(self):
        for transaction in self.transaction:
            print(transaction)
            import time 
            time.sleep(.5)
# Nithish=KotakBank("saranya",17238923,14314,2000)
# Nithish.deposit(2000)
# Nithish.deposit(2000)
# Nithish.deposit(2000)
# Nithish.deposit(2000)
# Nithish.withdraw(14314,2000)
# Nithish.display_transactions()
