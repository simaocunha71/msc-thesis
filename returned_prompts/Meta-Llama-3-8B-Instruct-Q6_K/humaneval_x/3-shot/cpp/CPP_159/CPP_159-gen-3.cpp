    int total = number + need;
    int left = total - remaining;
    if (left > 0)
        return {total, left};
    else
        return {total, remaining};
}