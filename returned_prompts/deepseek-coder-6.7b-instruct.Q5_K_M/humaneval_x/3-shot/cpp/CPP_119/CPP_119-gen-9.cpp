    int count = 0;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < lst[i].size(); j++) {
            if (lst[i][j] == '(') {
                count++;
            } else if (lst[i][j] == ')') {
                count--;
                if (count < 0) {
                    return "No";
                }
            }
        }
    }
    return (count == 0) ? "Yes" : "No";
}


