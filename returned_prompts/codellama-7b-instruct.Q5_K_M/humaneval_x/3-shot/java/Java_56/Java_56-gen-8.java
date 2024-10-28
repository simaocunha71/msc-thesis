        int opening_brackets = 0;
        for (char bracket : brackets.toCharArray()) {
            if (bracket == '<') {
                opening_brackets += 1;
            } else if (bracket == '>') {
                opening_brackets -= 1;
            }
        }
        return opening_brackets == 0;
    }
}

