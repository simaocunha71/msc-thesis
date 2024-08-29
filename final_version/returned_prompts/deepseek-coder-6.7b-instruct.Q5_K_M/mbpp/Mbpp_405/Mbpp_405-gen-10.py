def check_tuplex(tuplex, item):
    if item in tuplex:
        return True
    else:
        return False

print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')) # True


