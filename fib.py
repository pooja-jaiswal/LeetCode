# def fib_without_resursion(n, memo):
#     if memo[n] is not None:
#         return memo[n]
#     if n == 1 or n == 2:
#         result = 1
#     else:
#         result = fib_without_resursion(n-1, memo) + fib_without_resursion(n-2, memo)
#         memo[n] = result
#     return result

#     print(fib_without_resursion(5))


def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for each in range(3, n+1):
        bottom_up[each] = bottom_up[each-1] + bottom_up[each-2]
    return bottom_up[n]

if __name__ == "__main__":
    
    print(fib_bottom_up(26))