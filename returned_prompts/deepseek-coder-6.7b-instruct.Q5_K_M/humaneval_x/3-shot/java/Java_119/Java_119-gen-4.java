        int openCount1 = countOpenParens(lst.get(0));
        int closeCount1 = countCloseParens(lst.get(0));
        int openCount2 = countOpenParens(lst.get(1));
        int closeCount2 = countCloseParens(lst.get(1));

        if ((openCount1 + closeCount2 >= closeCount1) &&
            (openCount2 + closeCount1 >= openCount1) &&
            (closeCount1 + closeCount2 >= closeCount2)) {
            return "Yes";
        } else {
            return "No";
        }
    }

    private int countOpenParens(String str) {
        int count = 0;
        for (char c : str.toCharArray()) {
            if (c == '(') count++;
        }
        return count;
    }

    private int countCloseParens(String str) {
        int count = 0;
        for (char c : str.toCharArray()) {
            if (c == ')') count++;
        }
        return count;
    }
}

