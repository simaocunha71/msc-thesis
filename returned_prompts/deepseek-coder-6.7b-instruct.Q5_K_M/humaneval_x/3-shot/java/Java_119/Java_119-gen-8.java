        int count = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    count++;
                } else if (c == ')') {
                    count--;
                    if (count < 0) {
                        return "No";
                    }
                }
            }
        }
        return count == 0 ? "Yes" : "No";
    }
}

