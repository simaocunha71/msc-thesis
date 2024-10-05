    int eaten = number + need - remaining;
    int left = remaining - (need - eaten);
    if (left < 0) left = 0;
    return