def collatz(n: int) -> int:
    count = 0

    if n > 1:
        if n % 2 == 0:
            n = n / 2
            count = collatz(n) + 1
        else:
            n = (3 * n) + 1
            count = collatz(n) + 1


    return count


if __name__ == "__main__":
    initialnumber = input()

    answer = collatz(int(initialnumber))

    print(answer)

