        int open = 0;
        int close = 0;

        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') open++;
                else close++;
            }
        }

        return open == close ? "Yes" : "No";
    }
}

