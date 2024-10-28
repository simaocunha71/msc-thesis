    int count=0;
    for (auto str: lst) {
        for (auto chr: str) {
            if (chr == '(') {
                count += 1;
            } else if (chr == ')') {
                if (count == 0) {
                    return "No";
                }
                count -= 1;
            }
        }
    }
    return count == 0 ? "Yes" : "No";
}


