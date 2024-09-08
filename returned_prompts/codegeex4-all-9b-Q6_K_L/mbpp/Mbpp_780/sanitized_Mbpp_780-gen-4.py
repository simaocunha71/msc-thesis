def find_combinations(tuples):
    def find_combinations_helper(tuples, index, current_sum, current_tuple, combinations):
        if index == len(tuples):
            if current_sum == 0:
                combinations.append(current_tuple)
            return
        
        for i in range(index, len(tuples)):
            new_sum = current_sum + sum(tuples[i])
            new_tuple = current_tuple + tuples[i]
            find_combinations_helper(tuples, i + 1, new_sum, new_tuple, combinations)
    
    combinations = []
    find_combinations_helper(tuples, 0, 0, (), combinations)
    return combinations