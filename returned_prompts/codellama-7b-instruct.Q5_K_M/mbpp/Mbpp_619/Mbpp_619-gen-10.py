def move_num(s):
    nums = re.findall(r'\d+', s)
    s = re.sub(r'\d+', '', s)
    return s + ''.join(sorted(nums))
