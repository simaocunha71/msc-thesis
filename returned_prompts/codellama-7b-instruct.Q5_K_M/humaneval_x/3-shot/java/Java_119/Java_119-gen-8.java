        int count = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') count++;
                else count--;
            }
        }
        return count == 0 ? "Yes" : "No";
    }
}

