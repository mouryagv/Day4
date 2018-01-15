l=[1,2,3,[4,5]]

def nested_sum(l):
    total = 0
    for i in l:
        if not isinstance(i,list):
               total+=i

        elif  isinstance(i,list):
              total += nested_sum(i)

    return total

print(nested_sum(l))
