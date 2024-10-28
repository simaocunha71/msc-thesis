        int openParens1 = countOpenParens(lst.get(0));
        int closedParens1 = countClosedParens(lst.get(0));
        int openParens2 = countOpenParens(lst.get(1));
        int closedParens2 = countClosedParens(lst.get(1));

        if (openParens1 < openParens2 && closedParens1 <= closedParens2) {
            return "Yes";
        } else if (openParens1 <= openParens2 && closedParens1 < closedParens2) {
            return "Yes";
        } else {
            return "No";
        }
    }

    private int countOpenParens(String s) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                count++;
            }
        }
        return count;
    }

    private int countClosedParens(String s) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == ')') {
                count++;
            }
        }
        return count;
    }
}

