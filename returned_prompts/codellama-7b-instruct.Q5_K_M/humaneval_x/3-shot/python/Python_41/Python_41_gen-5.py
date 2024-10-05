    def number_of_collisions_helper(n: int, left_to_right: bool, count: int) -> int:
        if n == 1:
            return count
        if left_to_right:
            return number_of_collisions_helper(n - 1, False, count + 1)
        else:
            return number_of_collisions_helper(n - 1, True, count)

    return number_of_collisions_helper(n, True, 0)


