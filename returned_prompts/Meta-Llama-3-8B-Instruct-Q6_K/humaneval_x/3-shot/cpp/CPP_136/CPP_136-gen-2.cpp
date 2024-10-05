    int largest_negative=INT_MAX;
    int smallest_positive=INT_MIN;
    for (int i : lst)
    {
        if (i<0 && i>largest_negative)
            largest_negative=i;
        if (i>0 && i<smallest_positive)
            smallest_positive=i;
    }
    return {largest_negative, smallest_positive};
}  // INT_MAX and INT_MIN are macros for the maximum and minimum possible value for an int in C++


