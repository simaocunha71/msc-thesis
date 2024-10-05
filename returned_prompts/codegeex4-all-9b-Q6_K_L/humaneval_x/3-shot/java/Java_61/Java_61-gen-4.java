        int count = 0;
        for (char c : brackets.toCharArray()) {
            if (c == '(') {
                count += 1;
            } else if (c == ')') {
                count -= 1;
            }
            if (count < 0) return false;
        }
        return count == 0;

    }
}

