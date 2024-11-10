from typing import List
import random


def mat_mul(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

    # check to make sure dimentions of matrices are correct
    if len(A[0]) != len(B):
        print("matrices are incompatible (rows != cols)")

    # list comprehension for generating a correctly sized matrix of A.cols and B.rows
    c: List[List[int]] = [[0 for _ in range(len(A[0]))] for _ in range(len(B))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                           c[i][j] += A[i][k] * B[k][j]

    return c

# helper func to generate array of given size with random ints 0-9
def generate(rows: int, cols: int) -> List[List[int]]:
    return [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]


def main():
    
    # standard input for matrx generation
    rows_a = int(input("# of rows for matrix A: "))
    cols_a = int(input("# of cols for matrix A: "))
    rows_b = int(input("# of rows for matrix B: "))
    cols_b = int(input("# of cols for matrix B: "))
    print()

    print("generating random matrix A:")
    A = generate(rows_a, cols_a)
    for row in A:
        print(row)
    print()

    print("generating random matrix B:")
    B = generate(rows_b, cols_b)
    for row in B:
        print(row)
    print()

    print("product of A x B:")
    c = mat_mul(A, B)
    for row in c:
        print(row)
    print()


if __name__ == "__main__":
    main()
