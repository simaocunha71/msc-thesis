    fruit_string, total_fruits = s, int(n)
    fruits = fruit_string.split(' ')
    fruit_count = 0
    for fruit in fruits:
        if fruit == 'apples':
            fruit_count += int(fruit_string.replace('apples and', '').replace('apples', '').strip().split(' ')[0])
        elif fruit == 'oranges':
            fruit_count += int(fruit_string.replace('oranges and', '').replace('oranges', '').strip().split(' ')[0])
    return total_fruits - fruit_count
    # or
    return total_fruits - sum(int(x) for x in (fruit_string.split(' ')[0] for fruit_string in [fruit_string.replace('apples and', '').replace('apples', '').strip(), fruit_string.replace('oranges and', '').replace('oranges', '').strip()]))


