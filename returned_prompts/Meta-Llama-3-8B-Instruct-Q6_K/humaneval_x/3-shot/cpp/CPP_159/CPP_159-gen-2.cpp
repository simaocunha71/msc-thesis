    int total_eaten = number + need;
    int total_left = remaining - (need - number);
    if(total_left < 0) total_left = 0;
    return {total_eaten, total_left};
}