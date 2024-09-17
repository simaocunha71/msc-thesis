def is_undulating(n):
    # Step 1: Get the length of the number
    length = len(str(n))
    
    # Step 2: Get the first half of the number
    first_half = str(n)[:length // 2]
    
    # Step 3: Get the second half of the number
    second_half = str(n)[length // 2:]
    
    # Step 4: Check if the first half and the second half are the same
    if first_half == second_half:
        return True
    else:
        return False