    def compare_one(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if a == b:
                return None
            elif a > b:
                return a
            else:
                return b
        elif isinstance(a, str) and isinstance(b, (int, float)):
            if '.' in b:
                b = b.split('.')
                b[1] = b[1][:len(b[1])-1]
                b = ''.join(b)
                b = float(b)
            else:
                b = int(b)
            if a == b:
                return None
            elif a > b:
                return a
            else:
                return b
        elif isinstance(a, (int, float)) and isinstance(b, str):
            if '.' in a:
                a = a.split('.')
                a[1] = a[1][:len(a[1])-1]
                a = ''.join(a)
                a = float(a)
            else:
                a = int(a)
            if a == b:
                return None
            elif a > b:
                return a
            else:
                return b
        elif isinstance(a, str) and isinstance(b, str):
            if '.' in a:
                a = a.split('.')
                a[1] = a[1][:len(a[1])-1]
                a = ''.join(a)
                a = float(a)
            else:
                a = int(a)
            if '.' in b:
                b = b.split('.')
                b[1] = b[1][:len(b[1])-1]
                b = ''.join(b)
                b = float(b)
            else:
                b = int(b)
            if a == b:
                return None
            elif a > b:
                return a
            else:
                return b

