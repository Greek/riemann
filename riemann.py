def main():
    # a: lower, b: upper
    a, b = 3, 6

    # n: subintervals
    n = 3

    # ∆x (delta x)
    width = (b - a) / n

    # resulting sums
    left_sum, right_sum = 0, 0

    # the function we want to integrate (should be user input)
    def function(x: int):
        return (4*x**2+3*x+2)

    # left riemann
    # start from a zero-indexed loop up to `n`
    for i in range(n):
        left_sum += function(a + i * width) * width

    # right riemann
    # start from 1 up to `n+1` to avoid zero-index
    for i in range(1, n + 1):
        right_sum += function(a + i * width) * width

    return left_sum, right_sum


if __name__ == "__main__":
    result = main()
    print("left\tright")
    print(result)
