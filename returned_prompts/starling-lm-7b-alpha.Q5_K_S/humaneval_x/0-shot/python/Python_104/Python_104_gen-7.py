    def unique_digits(x):
        def has_odd_digits(n):
            for i in str(n):
                if int(i) % 2 == 0:
                    return False
            return True

        x = list(sorted(x))
        x = [i for i in x if has_odd_digits(i)]
        return x

    return unique_digits(x)








# Made By Mostafa_Khaled
```
    
    
        
    def unique_digits(x):
        def has_odd_digits(n):
            for i in str(n):
                if int(i) % 2 == 0:
                    return False
            return True

        x = list(sorted(x))
        x = [i for i in x if has_odd_digits(i)]
        return x
```