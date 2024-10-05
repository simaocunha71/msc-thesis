    int count = 0;
    for (char c : brackets) {
        if (c == '(') {
            count += 1;
        } else if (c == ')') {
            if (count == 0) {
                return false;
            }
            count -= 1;
        }
    }
    return count == 0;
}


