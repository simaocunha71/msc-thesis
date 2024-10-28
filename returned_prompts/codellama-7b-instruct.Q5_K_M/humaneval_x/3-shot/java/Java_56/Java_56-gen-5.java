        int opening = 0;

        for (char c : brackets.toCharArray()) {
            if (c == '<') opening += 1;
            if (c == '>') opening -= 1;
        }
        return opening == 0;
    }
}

