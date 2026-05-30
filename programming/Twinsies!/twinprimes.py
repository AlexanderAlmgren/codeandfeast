def primes(numbers: list) -> list:
    justprimes = []

    # YOUR CODE GOES HERE

    return justprimes

def twinprimes(allprimes: list) -> int:
    count = 0

    # YOUR CODE GOES HERE

    return count


if __name__ == '__main__':
    number = input()
    twodigitlist = []

    for i in range(0, len(number)-1):
        twodigitlist.append(int(number[i:i+2]))

    primelist = primes(twodigitlist)
    print(twinprimes(primelist))