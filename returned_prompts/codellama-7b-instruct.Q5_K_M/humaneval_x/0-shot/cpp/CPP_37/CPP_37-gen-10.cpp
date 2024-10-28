    for (int i = 1; i < l.size(); i++) {
        if (i % 2 == 0) {
            int j = i - 1;
            while (j >= 0) {
                if (l[i] > l[j]) {
                    float temp = l[i];
                    l[i] = l[j];
                    l[j] = temp;
                }
                j = j - 2;
            }
        }
    }
    return l;
}


