        List<Integer> res = new ArrayList<>();
        int curr_depth = 0;
        int max_depth = 0;
        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                curr_depth++;
                max_depth = Math.max(max_depth, curr_depth);
            } else if (c == ')') {
                curr_depth--;
            }
        }
        res.add(max_depth);
        while (!res.isEmpty()) {
            paren_string = paren_string.substring(1);
            curr_depth = 0;
            max_depth = 0;
            for (char c : paren_string.toCharArray()) {
                if (c == '(') {
                    curr_depth++;
                    max_depth = Math.max(max_depth, curr_depth);
                } else if (c == ')') {
                    curr_depth--;
                }
            }
            res.add(max_depth);
        }
        return res;
    }
}



# # #
# Python implementation of above solution
class Solution:
    """
    >>> Solution.parseNestedParens("(()()) ((())) () ((())()())")
    [2, 3, 1, 3]
    """
    def parseNestedParens(self, paren_string):
        res = []
        curr_depth = 0
        max_depth = 0
        for c in paren_string:
            if c == '(':
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)
            elif c == ')':
                curr_depth -= 1
            else:
                assert False, "Unknown character: {}".format(c)
        res.append(max_depth)
        while len(res) != 0:
            paren_string = paren_string[1:]
            curr_depth = 0
            max_depth = 0
            for c in paren_string:
                if c == '(':