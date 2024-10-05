    vector<int> tri_seq(n + 1);
    tri_seq[0] = 1;
    if (n > 0)
        tri_seq[1] = 3;
    for (int i = 2; i <= n; i++)
        if (i % 2 == 0)
            tri_seq[i] = tri_seq[i - 1] + 1;
        else
            tri_seq[i] = tri_seq[i - 1] + tri_seq[i - 2] + tri_seq[i - 3];
    return tri_seq;
}


