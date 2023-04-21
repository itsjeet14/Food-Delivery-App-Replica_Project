import json
import re

class Admin_details:

    def admin_save_details(self, data):
        with open("admin_details.json", "w") as file:
            json.dump(data, file)
    
    def fetch_admin_details(self):
        try:
            with open("admin_details.json", "r") as file:
                datas = json.load(file)
                return datas
        except FileNotFoundError:
            return []
    
    def admin_ID(self, datas):
        adminIDs = set()
        for adminID in datas:
            adminIDs.add(adminID['id'])
        
        if adminIDs:
            adminID = max(adminIDs) + 1
        else:
            adminID = 1
        return adminID
    
    def admin_phone(self, phone):
        try:
            phone = "".join(phone.split())
            pattern = r"^[1-9]\d{9}$"

            if re.match(pattern, phone):
                return True
            else:
                return False

        except ValueError:
            print("Invalid input!!")

    def admin_password(self, password):
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$"


        # Check if the password matches the regex pattern
        if re.match(pattern, password):
            return True
        else:
            return False
        
    
    def admin_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return True
        else:
            return False
        

        
    def admin_reg(self, datas):
        try:
            id = self.admin_ID(datas)
            name = input("Enter Name: ")
            phone = input("Enter your phone number: ")
            if not self.admin_phone(phone):
                print("Invalid Phone Number!!")
            
                while True:
                    phone = input("Enter Phone Number: ")
                    if self.admin_phone(phone):
                        break
                    else:
                        print("Invalid Phone Number!! Please enter a valid Phone Number.")
                            
            email = input("Enter Email ID: ")
            if not self.admin_email(email):
                print("Invalid Email ID")
            
                while True:
                    email = input("Enter Email: ")
                    if self.admin_email(email):
                        break
                    else:
                        print("Invalid Email ID. Please Enter right one!!")
           
            password = input("Enter Passoword: ")
            if not self.admin_password(password):
                print("Try another password!")
            
                while True:
                    password = input("Enter Password: ")
                    if self.admin_password(password):
                        break
                    else:
                        print("\nEnter valid password. \nPassword should contain \n*Minimum eight character \n*atleast one caps letter \natleast one small letter \natleast one numeric value \natleast one special character \n")
            
            data = {'id': id, 'name': name, 'phone': phone, 'email': email, "password": password}
            datas.append(data)

            self.admin_save_details(datas)

            print("Admin Registration Completed Successfully!!")
                
            
        except ValueError:
            print("Invalid Input!!")
    
    def admin_list(self):
        data = self.fetch_admin_details()
        print(f'Total Number of Admins are {len(data)}')
        for i in data:
            print(i, '\n')

    def admin_login(self):
        try:
            userid = input("Phone number: ")
            password = input("Enter Password: ")
            datas = self.fetch_admin_details()
            # result = False
            for data in datas:
                if data['phone'] == userid and data['password'] == password:
                    print("Successfully login!!")
                    # result = True
                    # break
                    return True
            # if not result:
                # print("Invalid Credential!!") 
            print("Invalid Credential!")
            return False
                                           
        except ValueError:
            print("Invalid Credentials!!")
            return False
        
