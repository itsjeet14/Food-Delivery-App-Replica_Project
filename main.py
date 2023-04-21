from admin_Food_operation import Admin_Food_Management
from admin_data_operation import Admin_details
from user_credential import user_credential_details
import sys

class Main:
    def operation(self, choice):
        try:
            if choice == 1:
                print("-----Admin Dashboard-----")
                while True:
                    choice = int(input("Enter \n1. Admin Registration \n2. Admin Login \n3. Admin list \n4. Back \n0. Exit \n"))
                    if choice == 1:
                        print("-----Complete Your Registration-----")
                        admin_detail_obj.admin_reg(admin_fetch_obj)
                
                    if choice == 2:
                        print("-----Admin Login-----")
                        if admin_detail_obj.admin_login():
                            print()
                            while True:
                                choice = int(input("Enter \n1. Add Food Items \n2. Edit Food Item \n3. View Food List \n4. Remove Food List \n5. Back To Previous Page \n0. Exit \n"))
                                if choice == 1:
                                    print("-----Add Food Items-----")
                                    admin_man_obj.add_food_item(fetch_data_obj)
                            
                                if choice == 2:
                                    print("-----Edit Food Items-----")
                                    admin_man_obj.edit_food_items(fetch_data_obj)

                                if choice == 3:
                                    print("-----View Food Items-----")
                                    admin_man_obj.view_food_items()
                            
                                if choice == 4:
                                    print("-----Delete Food Item-----")
                                    admin_man_obj.delete_food_items(fetch_data_obj)
                            
                                if choice == 5:
                                    break

                                if choice == 0:
                                    sys.exit()

                    if choice == 3:
                        print("-----Admin List-----")
                        admin_detail_obj.admin_list()

                    if choice == 4:
                        break
                
                    if choice == 0:
                        print("Thankyou!!")
                        sys.exit()

            if choice == 2:
                print("-----User Dashboard-----")
                while True:
                    choice = int(input("Enter \n1. User Registration \n2. User Login \n3. User list \n4. Back to previous page \n0. Exit \n"))
                    if choice == 1:
                        print("-----User Registration-----")
                        user_detail_obj.user_registration(fetch_user_detail_obj)

                    
                    if choice == 2:
                        print("----User Login-----")
                        if user_detail_obj.user_login():
                        # check = user_detail_obj.user_login()
                        
                            while True:
                                choice = int(input("Enter \n1. Place New Order \n2. Order History \n3. Update Profile \n4. Back to previous page \n0. Exit \n"))
                                if choice == 1:
                                    print("-----Place New Order-----")
                                    user_detail_obj.place_new_order()
                            
                                elif choice == 2:
                                    print("-----Order History-----")
                                    user_detail_obj.view_order_history()
                            
                                elif choice == 3:
                                    print("-----User Profile Update-----")
                                    user_detail_obj.update_user_profle(fetch_user_detail_obj)
                            
                                elif choice == 4:
                                    break
                            
                                elif choice == 0:
                                    print("Thankyou!!!")
                                    sys.exit()
                                
                                else:
                                    print("Invalid choice.")
                    
                            

                    
                    if choice == 3:
                        print("-----User List----")
                        user_detail_obj.view_user_list()
                    

                    if choice == 4:
                        break

                    if choice == 0:
                        print("Thankyou!!")
                        sys.exit()

    
        
            if choice == 0:
                print("-----Thankyou-----")
                sys.exit()
        except ValueError:
            print("Invalid Input!")


if __name__ == "__main__":
    main_obj = Main()  # Main() class calling
    admin_detail_obj = Admin_details()  # Admin credential class calling 
    admin_fetch_obj = admin_detail_obj.fetch_admin_details() # admin credential json file calling
    admin_man_obj = Admin_Food_Management() # admin food management class calling
    fetch_data_obj = admin_man_obj.fetch_data() # food detail json file calling
    user_detail_obj = user_credential_details()
    fetch_user_detail_obj = user_detail_obj.fetch_user_data()
    while True:
        try:
            choice = int(input("Enter \n1. Admin \n2. User \n0. Exit \n"))
            main_obj.operation(choice)
        except ValueError:
            print("Invalid Input!!")
