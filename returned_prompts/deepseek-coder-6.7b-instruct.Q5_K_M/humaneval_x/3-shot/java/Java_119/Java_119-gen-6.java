        int balance = 0;

        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    balance++;
                } else if (c == ')') {
                    balance--;
                    if (balance < 0) {
                        return "No";
                    }
                }
            }
        }
        return (balance == 0) ? "Yes" : "No";
    }
}

