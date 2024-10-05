    List<String> result = new ArrayList<>();
    int start = 0;
    int end = 0;
    while (start < paren_string.length()) {
        int i = start;
        while (i < paren_string.length() && paren_string.charAt(i) != '(' && paren_string.charAt(i) != ')') {
            i++;
        }
        if (i < paren_string.length() && paren_string.charAt(i) == '(') {
            start = i;
            end = findEnd(start, paren_string);
            result.add(paren_string.substring(start, end + 1));
        }
    }
    return result;
    }

    public int findEnd(int start, String paren_string) {
        int i = start;
        int end = 0;
        int count = 0;
        while (i < paren_string.length()) {
            if (paren_string.charAt(i) == '(') {
                count++;
            } else if (paren_string.charAt(i) == ')') {
                count--;
            }
            if (count == 0) {
                end = i;
                break;
            }
            i++;
        }
        return end;
    }
}


























































































































































































