    vector<int> tri;
    if (n < 1) return tri;
    tri.push_back(1);
    tri.push_back(3);
    for (int i = 2; i < n; i++) {
        if (i % 2 == 0) {
            tri.push_back(i / 2 + 1);
        } else {
            int temp = tri[i - 1] + tri[i - 2] + tri[i - 3];
            tri.push_back(temp);
        }
    }
    return tri;
}