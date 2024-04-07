#!/usr/bin/env python3
def factorize(n):
    # A simple approach to factorize the number into two factors
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1

def main(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            p, q = factorize(number)
            print(f"{number}={p}*{q}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
    else:
        main(sys.argv[1])
