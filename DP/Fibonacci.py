# f(0) = 0, f(1) = 1
# f(n) = f(n-1) + f(n-2)
import time


def fib1(n):
    if n == 0 or n == 1:
        return n
    return fib1(n-1) + fib1(n-2)


def fib2(n):
    my_memo = dict()
    my_memo[0] = 0
    my_memo[1] = 1

    for i in range(2, n+1):
        my_memo[i] = my_memo[i-1] + my_memo[i-2]
    return my_memo[n]


start_time = time.time()
print(fib1(10))
print('time:', time.time() - start_time)

start_time = time.time()
print(fib2(50))
print('time:', time.time() - start_time)
