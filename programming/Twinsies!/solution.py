def primes(numbers: list) -> list:
    justprimes = []

    for i in numbers:
        if i >= 10:
            if i % 6 == 1 or i % 6 == 5:
                j = 0
                for j in range(5, int(j ** 0.5) + 1):
                    if i % j == 0:
                        break
                else:
                    justprimes.append(i)


    return justprimes

def twinprimes(allprimes: list) -> int:
    count = 0

    for i in range(0, len(allprimes)):
        for j in range(i+1, len(allprimes)):
            if allprimes[i]+2 == allprimes[j]:
                count += 1

    return count


if __name__ == '__main__':
    number = input()
    twodigitlist = []

    for i in range(0, len(number)-1):
        twodigitlist.append(int(number[i:i+2]))

    primelist = primes(twodigitlist)
    print(twinprimes(primelist))
