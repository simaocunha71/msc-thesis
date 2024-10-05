        List<Integer> deepest = new ArrayList<>();
        int max_level = 0;
        int level = 0;
        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                level++;
                if (level > max_level) {
                    max_level = level;
                }
            } else if (c == ')') {
                level--;
            }
        }
        deepest.add(max_level);
        return deepest;
    }
}



# Python
def parseNestedParens(paren_string):
    deepest = []
    max_level = 0
    level = 0
    for c in paren_string:
        if c == '(':
            level += 1
            if level > max_level:
                max_level = level
        elif c == ')':
            level -= 1
    deepest.append(max_level)
    return deepest




# Python
def parseNestedParens(paren_string):
    deepest = []
    max_level = 0
    for c in paren_string:
        if c == '(':
            max_level += 1
        elif c == ')':
            max_level -= 1
        deepest.append(max_level)
    return deepest




# Python
def parseNestedParens(paren_string):
    deepest = []
    level = 0
    for c in paren_string:
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
        deepest.append(level)
    return deepest



# Python
def parseNestedParens(paren_string):
    deepest = []
    level = 0
    for c in paren_string:
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
        deepest.append(level)
    return deepest


# Python
def parseNestedParens(paren_string