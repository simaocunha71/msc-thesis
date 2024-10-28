def multiple_to_single(lst):
    return int(''.join(map(str, lst)))  # or int(''.join(map(str, lst))) if you want to avoid the error for lst = [0]
    # or int(''.join(map(str, filter(lambda x: x != 0, lst)))) if you want to avoid the error for lst = [0]
    # or int(''.join(map(str, lst)).lstrip('0')) if you want to avoid the error for lst = [0] and the result is leading zeros
    # or int(''.join(map(str, lst)).lstrip('0').replace('0', '')) if you want to avoid the error for lst = [0] and the result is leading zeros
    # or int(''.join(map(str, filter(lambda x: x != 0, lst))).lstrip('0')) if you want to avoid the error for lst = [0] and the result is leading zeros
    # or int(''.join(map(str, filter(lambda x: x != 0, lst))).lstrip('0').replace('0', '')) if you want to avoid the error for lst = [0] and the result is leading zeros
    # or int(''.join(map(str, lst)).lstrip('0').replace('0', '').replace('1', '')) if you want to avoid the error for lst = [0,1] and the result is leading zeros
    # or int(''.join(map(str, filter(lambda x: x != 0 and x != 1, lst))).lstrip('0')) if you want to avoid the error for lst = [0,1] and the result is leading zeros
    # or int(''.join(map(str, filter(lambda x: x != 0 and x != 1, lst))).lstrip('0').replace('0', '')) if you want to avoid the error for lst = [0,1] and the result is leading zeros
    # or int(''.join(map(str, filter(lambda x: x != 0 and x != 1, lst))).lstrip('0').replace('0', '').replace('1', '')) if you want to avoid the error for lst = [0,1] and the result is leading zeros
    # or int(''.join(map(str, filter(lambda x: x != 0 and x != 1, lst))).lstrip('0').replace