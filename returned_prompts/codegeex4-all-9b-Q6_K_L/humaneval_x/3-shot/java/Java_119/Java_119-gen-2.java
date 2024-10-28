        int count = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') count += 1;
                else count -= 1;
            }
        }
        return count == 0 ? "Yes" : "No";
    }
}

