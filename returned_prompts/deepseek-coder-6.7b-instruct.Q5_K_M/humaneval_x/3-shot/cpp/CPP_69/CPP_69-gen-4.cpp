    int i, j, maxCount = -1;
    for (i = 0; i < lst.size(); i++) {
        int count = 0;
        for (j = 0; j < lst.size(); j++) {
            if (lst[j] == lst[i])
                count++;
        }
        if (count >= lst[i] && count > maxCount) {
            maxCount = count;
        }
    }
    return maxCount != -1 ? maxCount : -1;
}



