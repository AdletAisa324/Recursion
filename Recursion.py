def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


def sum_numbers(n):
    if n <= 0:
        return 0
    return n + sum_numbers(n - 1)

print(sum_numbers(5))


def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)

print(power(2, 5))


def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(58321))


def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(58321))


def reverse_number(n, result=0):
    if n == 0:
        return result
    return reverse_number(n // 10, result * 10 + n % 10)

print(reverse_number(12345))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))


def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

print(gcd(48, 18))


def array_sum(arr, index=0):
    if index == len(arr):
        return 0
    return arr[index] + array_sum(arr, index + 1)

print(array_sum([2, 4, 6, 8]))


def find_maximum(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]
    max_rest = find_maximum(arr, index + 1)
    if arr[index] > max_rest:
        return arr[index]
    return max_rest

print(find_maximum([4, 8, 2, 15, 7]))


def count_occurrences(arr, x, index=0):
    if index == len(arr):
        return 0
    current = 1 if arr[index] == x else 0
    return current + count_occurrences(arr, x, index + 1)

print(count_occurrences([2, 5, 2, 8, 2, 9], 2))


def palindrome(s, left=0, right=None):
    if right is None:
        right = len(s) - 1
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return palindrome(s, left + 1, right - 1)

print(palindrome("level"))
print(palindrome("hello"))


def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("algorithm"))


def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    return binary_search(arr, target, mid + 1, right)

arr = [2, 4, 7, 10, 15, 21]
print("Index:", binary_search(arr, 15))


def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)

tower_of_hanoi(3, "A", "B", "C")
print("Total moves:", 2 ** 3 - 1)


def subsets(arr, index=0, current=None):
    if current is None:
        current = []
    if index == len(arr):
        print(current)
        return
    subsets(arr, index + 1, current)
    current.append(arr[index])
    subsets(arr, index + 1, current)
    current.pop()

subsets([1, 2, 3])


def permutations(s, current=""):
    if len(s) == 0:
        print(current)
        return
    for i in range(len(s)):
        remaining = s[:i] + s[i + 1:]
        permutations(remaining, current + s[i])

permutations("ABC")


def maze_solver(maze):
    rows = len(maze)
    cols = len(maze[0])
    path = []

    def search(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols):
            return False
        if maze[r][c] == 1:
            return False
        if (r, c) in path:
            return False

        path.append((r, c))

        if r == rows - 1 and c == cols - 1:
            return True

        if (search(r + 1, c) or
            search(r, c + 1) or
            search(r - 1, c) or
            search(r, c - 1)):
            return True

        path.pop()
        return False

    if search(0, 0):
        print("Path found:")
        print(path)
    else:
        print("No path found")


maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 0, 0]
]

maze_solver(maze)


def n_queens(n):
    board = [-1] * n
    solutions = []

    def is_safe(row, col):
        for prev_row in range(row):
            prev_col = board[prev_row]
            if prev_col == col:
                return False
            if abs(prev_col - col) == abs(prev_row - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)

    for solution in solutions:
        for col in solution:
            line = ["."] * n
            line[col] = "Q"
            print(" ".join(line))
        print()

    print("Total solutions:", len(solutions))


n_queens(4)


def preorder(node):
    if node is None:
        return
    print(node["value"], end=" ")
    preorder(node["left"])
    preorder(node["right"])


def inorder(node):
    if node is None:
        return
    inorder(node["left"])
    print(node["value"], end=" ")
    inorder(node["right"])


def postorder(node):
    if node is None:
        return
    postorder(node["left"])
    postorder(node["right"])
    print(node["value"], end=" ")


root = {
    "value": 10,
    "left": {
        "value": 5,
        "left": {
            "value": 2,
            "left": None,
            "right": None
        },
        "right": {
            "value": 7,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 15,
        "left": None,
        "right": {
            "value": 20,
            "left": None,
            "right": None
        }
    }
}

print("Preorder:", end=" ")
preorder(root)
print("\nInorder:", end=" ")
inorder(root)
print("\nPostorder:", end=" ")
postorder(root)
