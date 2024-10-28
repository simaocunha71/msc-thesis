    def will_it_fly(q, w):
        if str(q) == str(q)[::-1]:
            return sum(q) <= w
        else:
            return False
    # Check if the list is palindromic, if it is, check if the sum is less than or equal to w, if not, return False. If the list is not palindromic, return False.