        int opening_count = 0;
        int closing_count = 0;

        for (char c : brackets.toCharArray()) {
            if (c == '(') opening_count++;
            else if (c == ')') closing_count++;
        }

        return opening_count == closing_count;
    }
}

