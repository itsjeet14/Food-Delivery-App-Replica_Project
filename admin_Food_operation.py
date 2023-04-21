import json
# import random
# import string
class Admin_Food_Management:
    def save_data(self, data):
        with open("admin_Food_data.json",'w') as file:
            json.dump(data, file)
    
    def fetch_data(self):
        try:
            with open("admin_Food_data.json", 'r') as file:
                data = json.load(file)
                return data
            
        except FileNotFoundError:
            return []
        

    # =====1111111111111111111111111111============================================  
    def food_id_generate_serial_number_like_from_1_so_on(self, data): # generate serial food id
        food_id = set()
        for ids in data:
            food_id.add(ids["id"])
        if food_id:
            ids = max(food_id) + 1
        else:
            ids = 1
        
        return ids



    # ===============2222222222222222222222222====================
    
    # def food_id_generator_random_alphabet_numeral_symboll(self, characters): 
    #     # Define the set of characters to choose from
    #     characters = string.ascii_letters + string.digits + string.punctuation
    
    #     # Generate a random 10-character string using the character set
    #     order_number = ''.join(random.choice(characters) for i in range(10))
    
    #     return order_number
    
    # =================333333333333333333333333333333======================
    # def Food_id_generator_random_numeral(self, order_number):
    #     # Generate a random 6-digit number
    #     order_number = random.randint(100000, 999999)
    #     return order_number
    
    # =================44444444444444444444444444444444================
    # def food_id_generator_random_alphabet_only(self, characters):
    #     characters = string.ascii_letters
    #     order_number = ''.join(random.choice(characters) for i in range(5))
    #     return order_number

    

    def add_food_item(self, data):
        try:
            id = self.food_id_generate_serial_number_like_from_1_so_on(data)
            name = input("Enter Food Name: ")
            quantity = input("Enter Quantity: ")
            price = float(input("Enter Price: "))
            discount = float(input("Enter Discount: "))
            stock = int(input("Stock available: "))

            datas = {"id": id, "name":name, "quantity": quantity, "price": price, "discount": discount, "stock": stock}
            
            data.append(datas)
            self.save_data(data)

            print(f"{name} added successfully with food_id {id}")

        except ValueError:
            print("Invalid Price Formate.")

    def view_food_items(self):
        food_list = self.fetch_data()
        for i in food_list:
            print(i, '\n')

    def edit_food_items(self, datas):
        try:
            id = int(input("Enter Food ID: "))
            for ids in datas:
                if ids['id'] == id:
                    name = input("Enter Name: ")
                    quantity = input("Enter quantity: ")
                    price = float(input("Enter Price: "))
                    discount = float(input("Enter Discount: "))
                    stock = int(input("Enter Stock: "))

                    ids['name'] = name
                    ids['quantity'] = quantity
                    ids['price'] = price
                    ids['discount'] = discount
                    ids['stock'] = stock
                    self.save_data(datas)

                    print("Food Items updated Successfully!!")
                    return
            print("Food ID Not Found!!")
        except ValueError:
            print("Invalid Food ID!!")

    def delete_food_items(self, datas):
        try:
            id = int(input("Enter Food ID: "))
            for ids in datas:
                if ids['id'] == id:
                    datas.remove(ids)

                    self.save_data(datas)
                    print("Food Item Deleted Successfully!!")
                    return
            print("Food Id Not Found!")
        except ValueError:
            print("Invaid Input!!")
