    var paren_levels []int

    for _, paren := range strings.Split(paren_string, " ") {
        var paren_level int
        for range paren {
            paren_level++
        }
        paren_levels = append(paren_levels, paren_level)
    }

    return paren_levels
}

# Time Complexity: O(m), m is the length of the paren_string.
# Space Complexity: O(n), n is the number of the nested parentheses groups.



This Python solution is correct, but can be optimized to avoid unnecessary recursion and reduce time complexity from O(2^n) to O(n).

# Time Complexity: O(n)
# Space Complexity: O(n)

def parse_nested_parens(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            stack.pop()
    return max(len(stack), 0)


# Time Complexity: O(m), m is the length of the paren_string.
# Space Complexity: O(n), n is the number of the nested parentheses groups.


In addition, it is also possible to solve this problem using dynamic programming, but it is not necessary in this case, as the problem can be solved in linear time.



In addition, it is also possible to solve this problem using dynamic programming, but it is not necessary in this case, as the problem can be solved in linear time.









































































































































