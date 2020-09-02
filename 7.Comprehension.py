# Make list data Structure 
# Contains three portion 1.output Expression 2. Input Sequence 3.Conditional logic 
# zip takes the value in parallely and do the calculations 

a = [i for i in range(11)] 
b = [i for i in range(15)]
s = zip(a,b)
print(s) # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]

a_list = ['name','country','career']
b_list = ['nasim','Bangladesh','Software Developer']

my_dict = {i:j for i,j in zip(a_list,b_list)}

print(my_dict) # {'career': 'Software Developer', 'country': 'Bangladesh', 'name': 'nasim'}