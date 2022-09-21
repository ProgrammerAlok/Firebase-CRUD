from firebase import firebase

firebase = firebase.FirebaseApplication("https://pythondbtest-f41bd-default-rtdb.firebaseio.com/", None)

firebase.delete('https://gate-opener-71e67-default-rtdb.firebaseio.com/Customer/', '-NC-dxqvztRbTuvr6ASr')

print("Record Deleted")
