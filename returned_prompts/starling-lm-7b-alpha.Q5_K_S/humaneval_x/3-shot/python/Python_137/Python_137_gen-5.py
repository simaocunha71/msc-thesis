    def compare_one(a, b):
        # Check if both are integers
        if isinstance(a, int) and isinstance(b, int):
            if a > b:
                return a
            elif b > a:
                return b
            else:
                return None
        # Check if both are floats
        elif isinstance(a, float) and isinstance(b, float):
            if a > b:
                return a
            elif b > a:
                return b
            else:
                return None
        # Check if both are strings
        elif isinstance(a, str) and isinstance(b, str):
            if float(a) > float(b):
                return a
            elif float(b) > float(a):
                return b
            else:
                return None
        # Check if one is an integer and the other is a float
        elif (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
            if float(a) > b:
                return float(a)
            elif float(b) > a:
                return float(b)
            else:
                return None
        # Check if one is an integer and the other is a string
        elif (isinstance(a, int) or isinstance(a, float)) and isinstance(b, str):
            if float(a) > float(b):
                return float(a)
            elif float(b) > a:
                return b
            else:
                return None
        # Check if one is a float and the other is a string
        elif isinstance(a, str) and (isinstance(b, int) or isinstance(b, float)):
            if float(a) > b:
                return a
            elif float(b) > a:
                return b
            else:
                return None
        # Check if one is a string and the other is a string
        elif isinstance(a, str) and isinstance(b, str):
            if float(a) > float(b):
                return a
            elif float(b) > float(a):
              