def multiplicationTable(size):
    return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]

x  = multiplicationTable(5)

print(x)
print()

for i in x:
    print(i)
    
