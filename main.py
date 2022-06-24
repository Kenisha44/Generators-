#Generators allows to generate a sequence of values over time. 
#generator example is range(100)
#allows us to use a special keyword that allows us to pause and resume 

range(100)
list(range(100))

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result 

my_list = make_list(100)
print(my_list)