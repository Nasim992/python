# Set is unique never contains repeated elements 
# We cannot access set element by its index number 
# Declaring a set A = set() or A ={}

A = {'nasim','a','b','c','apple','mango','jackfruit'}
print(type(A))   # output : <type 'set'>

A.add('jambura')  # Add single elements
print (A) # set(['a', 'jackfruit', 'c', 'b', 'apple', 'mango', 'nasim', 'jambura'])

A.update({'peyara','guava'}) # Added Multiple Elements
print(A) # set(['a', 'jackfruit', 'c', 'b', 'apple', 'peyara', 'mango', 'nasim', 'jambura', 'guava'])

A.remove('apple') # Remove elements if not found the return KeyError
print(A) # set(['a', 'jackfruit', 'c', 'b', 'peyara', 'mango', 'nasim', 'jambura', 'guava'])

A.discard('guava') #  Remove elements if not found the do nothing.
print(A) # set(['a', 'jackfruit', 'c', 'b', 'peyara', 'mango', 'nasim', 'jambura'])

A.pop()
print(A) # nasim

A.clear()
print(A) # set([])

B = {1,2,3,4,5,6} 
C = {7,8,9,4,5,6} 
print(B.union(C)) # set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(B.intersection(C)) # set([4, 5, 6])
print(B.difference(C))# set([1, 2, 3])
