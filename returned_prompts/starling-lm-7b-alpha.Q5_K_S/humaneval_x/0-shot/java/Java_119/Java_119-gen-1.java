        int cnt = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == ')') {
                    cnt--;
                } else {
                    cnt++;
                }
                if (cnt < 0) {
                    return "No";
                    break A;
                }
            }
        }
        return "Yes";
    }

    /**
    Given a list of strings, return the longest string in the list.
    For example, if the input is ["aa", "bb", "cc", "dd", "ee"] then the
    return value should be "ee".

    Examples:
    longestString(["aa", "bb", "cc", "dd", "ee"]) == "ee"
    longestString(["aaa", "bbcde", "abcd"]) == "bbcde"
    longestString(["aa", "ab", "ac", "ad"]) == "abcd"
    */
    public String longestString(List<String> lst) {
        String ret = "";
        for (String s : lst) {
            if (ret.length() < s.length()) {
                ret = s;
            }
        }
        return ret;
    }

    /**
    Given a list of strings, return a new list containing only the strings of
    length 3 from the original list.
    For example, if the input is ["aa", "bb", "cc", "dd", "ee"] then the
    return value should be ["aa", "bb", "cc", "dd", "ee"].

    Examples:
    filterThree(["aa", "bb", "cc", "dd", "ee"]) == ["aa", "bb", "cc", "dd", "ee"]
    filterThree(["ab", "cde", "fgh", "ijk", "lmn"]) == []
    filterThree(["abcd", "efgh", "ijk", "lmno"]) == ["abcd", "efgh"]
    */
    public List<String> filterThree(List<String> lst) {
        List<String> ret = new ArrayList<>();
       