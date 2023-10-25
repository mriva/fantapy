def fibonacci(n):
    list = [1, 1]

    for n in range(2, n):
        list.append(list[-1] + list[-2])
        
    return list

print(fibonacci(10))