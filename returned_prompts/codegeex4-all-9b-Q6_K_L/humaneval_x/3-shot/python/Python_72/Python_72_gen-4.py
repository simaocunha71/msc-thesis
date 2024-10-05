    def is_palindrome(lst):
        return lst == lst[::-1]

    def sum_list(lst):
        return sum(lst)

    return is_palindrome(q) and sum_list(q) <= w

