def add3(a, b, c):
    return a + b + c

print(add3(2, 4, 6))

# for (int i = 0; i < v; i++)

def fibonacci(v) -> list[int]:
    prev1 = 1
    prev2 = 1

    f_list = [1, 1]

    for i in range(v-2):
        f_list.append(prev1 + prev2)
        prev1 = prev2
        prev2 = f_list[-1]
    
    return f_list


print(fibonacci(10))


