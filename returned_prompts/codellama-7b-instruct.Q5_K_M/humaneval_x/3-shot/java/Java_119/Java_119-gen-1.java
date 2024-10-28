        if (lst.get(0).equals("(") && lst.get(1).equals(")")) {
            return "Yes";
        } else if (lst.get(0).equals("()") && lst.get(1).equals("()")) {
            return "Yes";
        } else {
            return "No";
        }
    }
}

