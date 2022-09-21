from firebase import firebase

firebase = firebase.FirebaseApplication("https://gate-opener-71e67-default-rtdb.firebaseio.com/", None)


data = {
    # 'Name':'Sahel Bej',
    # 'Email':'sahel@gmail.com',
    # 'Phone':4445762346
    'PersonDetected':1
}

result = firebase.post('https://gate-opener-71e67-default-rtdb.firebaseio.com/Customer', data)

f=open("ID.txt", "w")
f.write(str(result))

print(result)
