    int i = 0;
    while (i * i * i <= abs(a)) {
        if (i * i * i == abs(a)) {
            return true;
        }
        i++;
    }
    return false;
}


