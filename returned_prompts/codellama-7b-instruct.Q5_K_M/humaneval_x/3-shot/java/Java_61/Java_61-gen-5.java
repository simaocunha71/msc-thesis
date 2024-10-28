        int opening = 0;

        for (char c : brackets.toCharArray()) {
            if (c == '(') opening += 1;
            else if (c == ')') opening -= 1;

            if (opening < 0) return false;
        }
        return opening == 0;
    }
}

