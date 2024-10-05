        int opening = 0;
        for (char c : brackets.toCharArray()) {
            if (c == '<') {
                opening++;
            } else if (c == '>') {
                if (opening == 0) return false;
                opening--;
            }
        }
        return opening == 0;
    }
}

