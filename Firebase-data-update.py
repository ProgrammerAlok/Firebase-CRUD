from firebase import firebase

firebase = firebase.FirebaseApplication("https://gate-opener-71e67-default-rtdb.firebaseio.com/", None)

firebase.put('https://gate-opener-71e67-default-rtdb.firebaseio.com/-NC-1q7HN91mmEdJmy3I', 'Name', 'Tech-A-Thon')

print("Record Updated") 