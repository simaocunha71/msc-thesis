def tuple_str_int(t):
    try:
        t = t.strip('()').split(',')
        return tuple(map(int, t))
    except ValueError:
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None