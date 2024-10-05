    def points(x):
        return (x, sum(int(i) for i in str(x)))

    nums.sort(key=points)

    return nums


