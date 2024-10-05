        int count = 0;
        for (String str : lst) {
            for (char c : str.toCharArray()) {
                if (c == '(') count += 1;
                else if (c == ')') count -= 1;
            }
            if (count < 0) return "No";
        }
        return count == 0 ? "Yes" : "No";
    }
}

