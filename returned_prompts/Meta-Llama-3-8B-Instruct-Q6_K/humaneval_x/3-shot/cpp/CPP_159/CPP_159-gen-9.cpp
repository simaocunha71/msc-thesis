    int total = number + need - remaining;
    int left = remaining - (number + need - total);
    if (left < 0) {
        total += left;
        left = 0;
    }
    return {total, left};
} // end of function eat


