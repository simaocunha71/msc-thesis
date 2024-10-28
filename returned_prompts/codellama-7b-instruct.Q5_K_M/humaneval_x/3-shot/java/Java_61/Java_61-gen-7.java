        int open_bracket_count = 0;
        for (char c : brackets.toCharArray()) {
            if (c == '(') open_bracket_count += 1;
            else if (c == ')') open_bracket_count -= 1;
            if (open_bracket_count < 0) return false;
        }
        return open_bracket_count == 0;
    }
}

