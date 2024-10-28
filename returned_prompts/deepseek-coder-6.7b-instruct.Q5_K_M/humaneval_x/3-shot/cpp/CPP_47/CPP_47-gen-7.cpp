    sort(l.begin(), l.end());
    int length = l.size();
    if (length % 2 == 0)
        return (l[length / 2 - 1] + l[length / 2]) / 2;
    else
        return l[length / 2];
}

