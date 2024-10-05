        String s = "";
        for (String a : lst) {
            s += a;
        }
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                count++;
            } else {
                count--;
            }
            if (count < 0) {
                return "No";
            }
        }
        if (count == 0) {
            return "Yes";
        }
        return "No";
    }
}
