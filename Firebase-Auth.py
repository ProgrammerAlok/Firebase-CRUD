from pyrebase import pyrebase

#Configure and Connext to Firebase

firebaseConfig = {
                'apiKey': "AIzaSyABVtFof1aCka34qb8KGuWXUlZS9kwlRtE",
                'authDomain': "authdemo-ad834.firebaseapp.com",
                'projectId': "authdemo-ad834",
                'storageBucket': "authdemo-ad834.appspot.com",
                'messagingSenderId': "424695142788",
                'appId': "1:424695142788:web:e3fed5a34bf4b06b67a5d1",
                'measurementId': "G-V18D4SZTC2"
                  }

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

#Login function()

def login():
     print("Log in...")
     email=input("Enter email: ")
     password=input("Enter password: ")
     try:
         login = auth.sign_in_with_email_and_password(email, password)
         print("Successfully logged in!")
         print(auth.get_account_info(login['idToken']))
         email = auth.get_account_info(login['idToken'])['users'][0]['email']
         print(email)
     except:
         print("Invalid email or password")
     return

#Signup Function

def signup():
    print("Sign up...")
    email = input("Enter email: ")
    password=input("Enter password: ")
    user = auth.create_user_with_email_and_password(email, password)

def signup():
     print("Sign up...")
     email = input("Enter email: ")
     password=input("Enter password: ")
     try:
         user = auth.create_user_with_email_and_password(email, password)
         ask=input("Do you want to login?[y/n]")
         if ask=='y':
             login()
     except: 
        print("Email already exists")
     return

#main

ans=input("Are you a new user?[y/n]")

if ans == 'n':
    login ()
elif ans == 'y':
    signup()