
# ------------------ STACK ADT ------------------
class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# ------------------ FACTORIAL ------------------
def factorial(n):
    if n < 0:
        return "Invalid Input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# ------------------ FIBONACCI ------------------
call_count_naive = 0
call_count_memo = 0

def fib_naive(n):
    global call_count_naive
    call_count_naive += 1
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

memo = {}
def fib_memo(n):
    global call_count_memo
    call_count_memo += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]


# ------------------ TOWER OF HANOI ------------------
def hanoi(n, source, auxiliary, destination, stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        stack.push(move)
        return

    hanoi(n-1, source, destination, auxiliary, stack)

    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    stack.push(move)

    hanoi(n-1, auxiliary, source, destination, stack)


# ------------------ BINARY SEARCH ------------------
def binary_search(arr, key, low, high, stack):
    if low > high:
        return -1

    mid = (low + high) // 2
    stack.push(mid)

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1, stack)
    else:
        return binary_search(arr, key, mid + 1, high, stack)


# ------------------ MAIN ------------------
def main():
    print("===== STACK TEST =====")
    s = StackADT()
    s.push(10)
    s.push(20)
    print("Peek:", s.peek())
    print("Pop:", s.pop())
    print("Size:", s.size())

    print("\n===== FACTORIAL =====")
    for n in [0,1,5,10]:
        print(f"factorial({n}) =", factorial(n))

    print("\n===== FIBONACCI =====")
    for n in [5,10,20,30]:
        global call_count_naive, call_count_memo, memo

        call_count_naive = 0
        call_count_memo = 0
        memo = {}

        print(f"\nFibonacci({n})")
        print("Naive:", fib_naive(n), "Calls:", call_count_naive)
        print("Memo :", fib_memo(n), "Calls:", call_count_memo)

    print("\n===== TOWER OF HANOI (N=3) =====")
    stack_hanoi = StackADT()
    hanoi(3, 'A', 'B', 'C', stack_hanoi)

    print("\n===== BINARY SEARCH =====")
    arr = [1,3,5,7,9,11,13]
    for key in [7,1,13,2]:
        stack_bs = StackADT()
        result = binary_search(arr, key, 0, len(arr)-1, stack_bs)
        print(f"Search {key}: Index =", result, "Trace:", stack_bs.stack)

    # empty array case
    stack_bs = StackADT()
    print("Empty array search:", binary_search([], 5, 0, -1, stack_bs))


if __name__ == "__main__":
    main()