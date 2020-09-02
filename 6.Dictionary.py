# In dictionary each value should contain key 
# Declaring a dictionary A = {} or A = dict() 

A = {'name': 'Nasim Hossain','email':'mdnasim6416@gmail.com','phone':'01755706416'}
print (A['name']) # Nasim Hossain 

A['name'] = 'Md.Nasim Hossain'
print(A['name']) # Md.Nasim Hossain

B = {'hometown':'Kushtia,Jessore,Dhaka'}
A.update(B)
print(A['hometown']) # Kushtia,Jessore,Dhaka

del A['phone']
print(A) # {'hometown': 'Kushtia,Jessore,Dhaka', 'name': 'Md.Nasim Hossain', 'email': 'mdnasim6416@gmail.com'}

print(A.keys()) # ['hometown', 'name', 'email']
print(A.values()) # ['Kushtia,Jessore,Dhaka', 'Md.Nasim Hossain', 'mdnasim6416@gmail.com']

A.clear() 
print(A) # {}

print(A.get('email','nai')) # If not found then returns nai   --> nai

print(A.items()) # return a list  -->[] 