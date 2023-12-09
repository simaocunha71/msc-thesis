
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if len(lst) == 0:
        return 0
    
    cntOdd = [0] * (len(lst)) + [0]

    for idx, elm in enumerate(lst):
        if elm % 2 == 1 and idx % 2 != 1:
            cntOdd[idx+1] += 1
    
    return sum([elm % 2 for elm in range(0, len(cntOdd))]) - sum([el.odd if (idx, el) in cntOdd else 0 for idx, el in enumerate(cntOdd)])

if __name__ == '__main__':
    # input = [5, 8, 7, 1] => solution = 12
    input = [30, 13, 24, 321]
    print(solution(input))