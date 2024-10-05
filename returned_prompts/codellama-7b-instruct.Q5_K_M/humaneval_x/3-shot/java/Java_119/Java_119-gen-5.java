        int count_open_parens = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') count_open_parens++;
                else count_open_parens--;
            }
        }
        return (count_open_parens == 0) ? "Yes" : "No";
    }
}

