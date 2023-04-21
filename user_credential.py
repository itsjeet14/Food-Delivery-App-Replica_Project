import json
from admin_Food_operation import Admin_Food_Management
import re
class user_credential_details:
    def save_user_data(self, data):
        with open("user_credential.json", 'w') as file:
            json.dump(data, file)
    
    def fetch_user_data(self):
        try:
            with open("user_credential.json", 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return []
    
    def user_id_generate(self, datas):
        
        users_ids = set()
        for user_id in datas:
            users_ids.add(user_id['id'])
        if users_ids:
            user_id = max(users_ids) + 1
        else:
            user_id = 1
        return user_id
    
    def user_phone(self, phone):
        phone = ''.join(phone.split())
        pattern = r'^[1-9]\d{9}$'
        if re.match(pattern, phone):
            return True
        else:
            return False
    
    def user_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.*]+\.\w+$'
        if re.match(pattern,email):
            return True
        else:
            return False
    
    def user_password(self, password):
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'
        if re.match(pattern,password):
            return True
        else:
            return False
    
    def user_registration(self, datas):
        try:
            id = self.user_id_generate(datas)
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            if not self.user_phone(phone):
                print("Invalid Phoone Number!")
                while True:
                    phone = input("Enter Phone Number: ")
                    if self.user_phone(phone):
                        break
                    else:
                        print("Pls Enter valid phone number!")
            
            email = input("Enter Email: ")
            if not self.user_email(email):
                print("Invalid Email id")
                while True:
                    email = input("Enter Email: ")
                    if self.user_email(email):
                        break
                    else:
                        print("Pls Enter valid Email id")
            
            password = input("Enter Password: ")
            if not self.user_password(password):
                print("Password Not Strong!!")

                while True:
                    password = input("Enter Password: ")
                    if self.user_password(password):
                        break
                    else:
                        print("Pls Enter Strong Password!")
            
            data = {'id': id, 'name': name, 'phone': phone, 'email': email, 'password': password}
            datas.append(data)
            self.save_user_data(datas)
            print("Registration completed Successfully!!")
            return
        
        except ValueError:
            print("Invalid Input!!")
    
    def view_user_list(self):
        user = self.fetch_user_data()
        for users in user:
            print(users, '\n')

    def user_login(self):
        try:
            phone = input("Enter phone number: ")
            password = input("Enter Password: ")
            users = self.fetch_user_data()
            # res = False
            for user in users:
                if user['phone'] == phone and user['password'] == password:
                    print("Successfully Login!!")
                    # res = True
                    return True
            # if not res:
            #     print("User Not Found!!")     
            print("Invalid Credential!")
            return False
        
        except ValueError:
            print("Invalid Input!!")
            return False
    
    def save_order_history(self, data):
        with open("order_histor.json", 'w') as file:
            json.dump(data, file)
    
    def fetch_order_history(self):
        try:
            with open("order_histor.json", 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return []

    def place_new_order(self):
        a = Admin_Food_Management()
        b = a.fetch_data()
        print("-----Food list------")
        for i in b:
            print(f"(Food_id:{i['id']}) {i['name']} {(i['quantity'])} (INR {i['price']})")
        print()
        print("-----Choose option-----")
        choice = list(map(int, input("Enter FoodID separated by space you want to purchase: ").split()))
        print("\n------Your Order-------")
        total_price = 0
        discount= 0
        for id in choice:
            for food in b:
                if id == food['id']:
                
                    total_price += food['price']
                    discount += food['discount']*food['price']/100

        grand_Total = total_price-discount
        orders = []
        for id in choice:
            for food in b:
                if id == food['id']:
                    print(f"{food['name']} {food['quantity']} (INR {food['price']})")
        
                    order = {'name':food['name'], 'quantity':food['quantity'], 'total_price: INR': grand_Total}
                    orders.append(order)
                            

        print(f"Total Price: INR {total_price} \nTotal Discount: INR {discount}")
        print("Grand Total: INR", grand_Total)

        confirm = int(input("Do you want to proceed? \n1. Yes \n2. NO \n"))
        while True:
            if confirm == 2:
                print("Thank you! come back soon!!")
                break
            elif confirm == 1:
                print("Your order is confirmed")
                self.save_order_history(orders)
                break

    def view_order_history(self):
        data = self.fetch_order_history()
        datas = False
        for i in data:
            print(i, '\n')
            datas = True
            break
        if not datas:
            print("No Order Placed!!")
        

    def update_user_profle(self, datas):
        try:
            phone = input("Confirm phone number: ")
            for data in datas:
                if data['phone'] == phone:
                    name = input("Enter New Name: ")
                    phone = input("Enter New Phone Number: ")

                    data['name'] = name
                    data['phone'] = phone
                    self.save_user_data(datas)

                    print("User Profile Updated Successfully")
                    return
            print("Enter valid phone number")


        except ValueError:
            print("Invalid Input!!")
    

            

        

