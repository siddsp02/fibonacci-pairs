# !usr/bin/env python3

Pair = tuple[int, int]

def fib_pairs(n: int) -> Pair:
    pairs = [(0, 1), (1, 1)]
    k = 0
    for i in range(2, n+1):
        x, y = pairs[k]
        p = x + y
        if i & 1:
            x, y = x*x + y*y, y * (x+p)
        else:
            x, y, k = y * (x+p), y*y + p*p, k+1
        pairs.append((x, y))
    return pairs[n]


def main() -> None:
    n = 15
    print(fib_pairs(n))


if __name__ == "__main__":
    main()
