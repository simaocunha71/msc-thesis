def max_run_uppercase(string):
    run = 0
    max_run = 0
    for i in range(len(string)):
        if string[i].isupper():
            run += 1
            if run > max_run:
                max_run = run
        else:
            run = 0
    return max_run