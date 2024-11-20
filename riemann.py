def main():
    # a = lower, b = upper
    lower, upper = 3, 6

    # subintervals = n
    subintervals = 3

    # ∆x (delta x)
    width = (upper - lower) / subintervals

    # resulting sums
    left_sum, right_sum = 0, 0

    # the function we want to integrate (should be user input)
    def function(x: int):
        return (4*x**2+3*x+2)

    # calculate the sum of the left-endpoints by i
    # where we count from `a` up to `n`
    for i in range(subintervals):
        left_sum += function(lower + i * width) * width

    # calculate the sum of the right-endpoints by i
    # where we count from `1` up to `n + 1`
    for i in range(1, subintervals + 1):
        right_sum += function(lower + i * width) * width

    return left_sum, right_sum


if __name__ == "__main__":
    result = main()
    print("left\tright")
    print(result)
