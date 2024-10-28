    count1 = sum(1 for c in lst[0] if c == '(') - sum(1 for c in lst[0] if c == ')')
    count2 = sum(1 for c in lst[1] if c == '(') - sum(1 for c in lst[1] if c == ')')

    return count1 + count2 == 0