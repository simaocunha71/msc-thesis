    def is_palindromic(lst):
        return lst == lst[::-1]

    def sum_of_elements(lst):
        return sum(lst)

    return is_palindromic(q) and sum_of_elements(q) <= w

