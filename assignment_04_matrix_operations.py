# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# PART B — Add Two Matrices
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
#
# REQUIREMENTS
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
#
# =============================================================================


def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print("".join(f"{val:5}" for val in row))


def transpose_matrix(matrix, rows, cols):
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


def add_matrices(a, b, rows, cols):
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result


def multiply_matrices(a, b, m, n, p):
    result = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += a[i][k] * b[k][j]
            result[i][j] = total
    return result


def main():
    # ---------------- PART A: Transpose ----------------
    print("--- PART A: Transpose a Matrix ---")
    rows_a = int(input("Enter number of rows: "))
    cols_a = int(input("Enter number of columns: "))

    mat_a = read_matrix(rows_a, cols_a)

    print("\nOriginal Matrix:")
    print_matrix(mat_a)

    transposed = transpose_matrix(mat_a, rows_a, cols_a)
    print("\nTransposed Matrix:")
    print_matrix(transposed)

    # ---------------- PART B: Addition ----------------
    print("\n--- PART B: Add Two Matrices ---")
    rows_b = int(input("Enter number of rows: "))
    cols_b = int(input("Enter number of columns: "))

    print("\nEnter values for Matrix 1:")
    mat1 = read_matrix(rows_b, cols_b)

    print("\nEnter values for Matrix 2:")
    mat2 = read_matrix(rows_b, cols_b)

    sum_result = add_matrices(mat1, mat2, rows_b, cols_b)
    print("\nSum of Matrices:")
    print_matrix(sum_result)

    # ---------------- PART C: Multiplication ----------------
    print("\n--- PART C: Multiply Two Matrices ---")
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A: "))
    n2 = int(input("Enter rows of Matrix B: "))
    p = int(input("Enter columns of Matrix B: "))

    if n != n2:
        print("Error: Columns of A must equal rows of B for multiplication.")
        return

    print("\nEnter values for Matrix A:")
    mat_x = read_matrix(m, n)

    print("\nEnter values for Matrix B:")
    mat_y = read_matrix(n, p)

    product = multiply_matrices(mat_x, mat_y, m, n, p)
    print("\nProduct of Matrix A x B:")
    print_matrix(product)


if __name__ == "__main__":
    main()
