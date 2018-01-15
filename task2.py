import functools

def my_sum(x,y):
    return x+y

my_list=list(range(100,500,2))

total_sum=functools.reduce(my_sum,my_list)
print(total_sum)

