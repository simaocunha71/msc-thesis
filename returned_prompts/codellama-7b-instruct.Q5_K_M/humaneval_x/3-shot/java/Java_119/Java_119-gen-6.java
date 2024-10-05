        if (lst.get(0).equals("()") && lst.get(1).equals("()")) return "Yes";
        if (lst.get(0).equals("()") || lst.get(1).equals("()")) return "No";

        if (lst.get(0).length() + lst.get(1).length() == 2) {
            if (lst.get(0).charAt(0) == '(' && lst.get(0).charAt(1) == ')') {
                return "Yes";
            }
            if (lst.get(1).charAt(0) == '(' && lst.get(1).charAt(1) == ')') {
                return "Yes";
            }
            return "No";
        }

        if (lst.get(0).charAt(0) == lst.get(1).charAt(0) &&
            lst.get(0).charAt(1) == lst.get(1).charAt(1)) {
            return "No";
        }

        if (lst.get(0).length() == 1) {
            if (lst.get(1).charAt(0) == ')') {
                return "Yes";
            }
            return "No";
        }

        if (lst.get(1).length() == 1) {
            if (lst.get(0).charAt(0) == '(') {
                return "Yes";
            }
            return "No";
        }

        return "No";
    }
}

