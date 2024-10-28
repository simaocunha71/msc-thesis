def frequency_lists(input_list):
    # your code goes here
    output = {}
    for item in input_list:
        for i in item:
            if i in output:
                output[i] += 1
            else:
                output[i] = 1
    return output