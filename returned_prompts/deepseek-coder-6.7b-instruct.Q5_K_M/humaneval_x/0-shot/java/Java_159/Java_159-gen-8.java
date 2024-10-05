    int total_carrots_eaten = number;
    if (need <= remaining) {
        total_carrots_eaten += need;
        remaining -= need;
    } else {
        total_carrots_eaten += remaining;
        remaining = 0;
    }
    return Arrays