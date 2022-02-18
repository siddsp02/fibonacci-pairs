# !usr/bin/env python3

Pair = tuple[int, int]

def fib_pairs(n: int) -> list[Pair]:
    pairs = [(0, 1), (1, 1)]
    k = 0
    for i in range(2, n+1):
        x, y = pairs[k]
        p = x + y
        if i & 1:
            x, y, k = x*x + y*y, y * (x+p), k+1
        else:
            x, y = y * (x+p), y*y + p*p
        pairs.append((x, y))
    return pairs[n]


def main() -> None:
    n = 15
    print(fib_pairs(n))


if __name__ == "__main__":
    main()
