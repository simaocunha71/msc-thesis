    if(x%2==0)
        return x;
    else if(y%2==0)
        return y;
    else if(x<y)
        return y;
    else if(y<x)
        return -1;
    else
        return x;
} // This function checks if the numbers are even, and returns the biggest even number in the range. If no such number exists, it returns -1.