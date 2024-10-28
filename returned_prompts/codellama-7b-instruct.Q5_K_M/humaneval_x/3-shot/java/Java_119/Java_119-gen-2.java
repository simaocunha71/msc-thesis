        int open_count = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    open_count++;
                } else {
                    open_count--;
                }
            }
        }
        return open_count == 0 ? "Yes" : "No";
    }
}

