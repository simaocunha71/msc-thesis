    int n = l.size();
    if (n < 3) return false;

    sort(l.begin(), l.end());

    for (int i = 0; i < n - 1; i++) {
        int a = l[i];
        int start = i + 1;
        int end = n - 1;
        while (start < end) {
            if (a + l[start] + l[end] == 0) {
                return true;
            }
            else if (a + l[start] + l[end] < 0) {
                start += 1;
            }
            else {
                end -= 1;
            }
        }
    }
    return false;
}


