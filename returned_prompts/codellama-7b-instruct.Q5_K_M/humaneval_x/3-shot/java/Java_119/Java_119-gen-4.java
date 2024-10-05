        int open_cnt = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') open_cnt += 1;
                else open_cnt -= 1;
            }
        }
        return (open_cnt == 0) ? "Yes" : "No";
    }
}

