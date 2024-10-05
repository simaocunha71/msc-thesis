    if (size % 2 == 0) {
        // even
        return (l[size / 2] + l[size / 2 - 1]) / 2;
    } else {
        // odd
        return l[size / 2];
    }
}


