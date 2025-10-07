def main():
    n = int(input("Number: "))
    print(ways(n))


def ways(n, memo = {0: 1, 1: 1, 2: 2}):
    if n in memo:
        return memo[n]
    memo[n] = ways(n - 1, memo) + ways(n - 2, memo) + ways(n - 3, memo)
    return memo[n]


if __name__ == "__main__":
    main()
