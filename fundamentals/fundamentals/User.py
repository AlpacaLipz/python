# user1 = {
#     'first' : 'Randy',
#     'last' : 'Lynd',
#     'email' : 'Randy.lynd1988@gmail.com',
#     'age' : 34,
# }

class User: 
    def __init__(self, first, last, email, age, is_rewards_memeber = False , gold_card_points = 0):
        self.first = first
        self.last = last
        self.email = email
        self.age = age
        self.is_rewards_memeber = is_rewards_memeber
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(f"{self.first}")
        print(f"{self.last}")
        print(f"{self.email}")
        print(f"{self.age}")
        print(f"{self.gold_card_points}")
        return self
    
    def enroll(self):
        if self.is_rewards_memeber:
            print("i am already a memeber")
        else:
            self.is_rewards_member = True
            print("sign up here")
            self.gold_card_points = 200
            return self
    
    def spend_points(self, amount):
            self.gold_card_points = self.gold_card_points - amount
            return self


user1 = User("Randy", "Lynd", "Randy.lynd1988@gmail.com", 34)
user2 = User("Alpaca", "Jackson", "alpaca.jackson@yourfield.com", 8)
user3 = User("Manny", "Alpaquio", "manny.alpaquio@yourfield.com", 6 )
user1.enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()
user3.enroll().spend_points(20).display_info()
