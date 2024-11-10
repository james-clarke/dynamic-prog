import sys
from typing import List

def memoized_cut_rod(p: List[int], n: int) -> int:
    # initialize array of -inf
    r: List[int] = [-sys.maxsize - 1] * (n + 1)
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p: List[int], n: int, r: List[int]) -> int:
    # base case check
    if r[n] >= 0:
        return r[n]
    elif n == 0:
        q = 0

    else:
        q = -sys.maxsize - 1
        for i in range(1, n + 1):
            q = max(q, p[i - 1] + memoized_cut_rod_aux(p, n - i, r))
    
    r[n] = q
    return q


def main():
    p = [1, 2, 3, 4, 5]
    n = 5
    print(f"Max revenue: {memoized_cut_rod(p, n)}")

if __name__ == "__main__":
    main()

