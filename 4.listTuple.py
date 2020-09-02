a = [] # Declaration of  List 
c = () # Declaration of set 
b = ['tomato','Laptop','cucumber','gas']

b.append('Hossain')  # insert element at the end 

print(b[0])
b.insert(1,'Nasim')  # Insert to the list in anywhere 

b.extend(['a','b','c']) # insert multiple elements at a time 

del b[3]  # Delete an element
del b[-1] # Delete last element 
b.pop()
print(b)

b.reverse()
print(b) # reverse the list 
b.sort()
print(b)

Output:

tomato
['tomato', 'Nasim', 'Laptop', 'gas', 'Hossain', 'a']
['a', 'Hossain', 'gas', 'Laptop', 'Nasim', 'tomato']
['Hossain', 'Laptop', 'Nasim', 'a', 'gas', 'tomato']
