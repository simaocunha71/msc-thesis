        if (s0.length() != s1.length()) {
            return false;
        }

        Map<Character, Integer> char_count = new HashMap<>();

        for (char c : s0.toCharArray()) {
            char_count.put(c, char_count.getOrDefault(c, 0) + 1);
        }

        for (char c : s1.toCharArray()) {
            if (char_count.getOrDefault(c, 0) > 0) {
                char_count.put(c, char_count.get(c) - 1);
            } else {
                continue A;
            }
        }

        return true;
    }
}



# Python
def same_chars(s0, s1):
    if len(s0) != len(s1):
        return False

    char_count = {}

    for c in s0:
        char_count[c] = char_count.get(c, 0) + 1

    for c in s1:
        if char_count.get(c, 0) > 0:
            char_count[c] = char_count[c] - 1
        else:
            return False

    return True



# Python
def same_chars(s0, s1):
    if len(s0) != len(s1):
        return False

    char_count = {}

    for c in s0:
        char_count[c] = char_count.get(c, 0) + 1

    for c in s1:
        if char_count.get(c, 0) > 0:
            char_count[c] = char_count[c] - 1
        else:
            return False

    return True



# Python
def same_chars(s0, s1):
    if len(s0) != len(s1):
        return False

    char_count = {}

    for c in s0:
        char_count[c] = char_count.get(c,