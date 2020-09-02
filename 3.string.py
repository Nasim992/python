str = "Bangladesh is a \"Beautiful\" country"
print(str) ;


a = 'Bangladesh'
ab = "This is a very crowdy place"
print(a[1:4]) # Output--> ang 
print(a[:1])  # Output --> B 
print(a[:2])  # Output --> ngladesh
print(a[-1])  # Output --> h

print('My favourite country is :'+ a)
print('My favourite country is :%s'%a)
print(a.capitalize())
print(a.upper())
print(a.lower())
print(len(a))
print(a.count('l'))
print(a.replace('h','p'))
print(a.find('d',1))
print(ab.split())

output-->
My favourite country is :Bangladesh
My favourite country is :Bangladesh
Bangladesh
BANGLADESH
bangladesh
10
1
Bangladesp
6
['This', 'is', 'a', 'very', 'crowdy', 'place']