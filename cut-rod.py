import sys
from typing import List

def memoized_cut_rod(p: List[int], n: int) -> int:

    # initialize empty array
    r: List[int] = []

    # assign array vals to +inf
    for i in range(n):
        r[i] = sys.maxsize

    
    
    return 0

def main():
    memoized_cut_rod([1,2,3,4,5], 5)

if __name__ == "__main__":
    main()
