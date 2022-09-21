from firebase import firebase
# from slugify import slugify

firebase = firebase.FirebaseApplication("https://gate-opener-71e67-default-rtdb.firebaseio.com/", None)


f=open("ID.txt", "r")
s=f.read(100)
# s=dict(s)
r = slice(10, 30)
s=(s[r])
# print(s)

att1 = "'https://gate-opener-71e67-default-rtdb.firebaseio.com/Customer/"
# -NC-e7-R20NUSEmVSCMq
# att3="/PersonDetected/', ''"

# att = (att1+s+att3)

# att = slugify(att)

# print(att)

result = firebase.get('https://gate-opener-71e67-default-rtdb.firebaseio.com/Customer/-NC-q8sLyhhoozQxGRxy/PersonDetected/', '')

# result = firebase.get(att, '')

# result = firebase.get(att)
print(result)
if result==1:
    print("Hellow person.")
