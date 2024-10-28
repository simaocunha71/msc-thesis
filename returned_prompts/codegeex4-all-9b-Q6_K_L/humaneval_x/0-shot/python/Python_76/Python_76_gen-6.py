def is_simple_power(x, n):
    try:
        if x**int(x/n) == n:
            return True
        else:
            return False
    except ZeroDivisionError:
        return False
    except ValueError:
        return False
    except TypeError:
        return False

print(is_simple_power(1, 4))
print(is_simple_power(2, 2))
print(is_simple_power(8, 2))
print(is_simple_power(3, 2))
print(is_simple_power(3, 1))
print(is_simple_power(5, 3))