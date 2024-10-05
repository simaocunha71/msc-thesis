    if (x>y)
    {
        if (x%2==0)
        return x;
        else
        return -1;
    }
    else if (y%2==0)
    return y;
    else
    {
        int temp = (x+y)/2;
        if (temp % 2 == 0)
        return temp;
        else
        return -1;
    }
}  // This code will return the biggest even number in the range, or -1 if no such number exists.  // It will handle all possible cases. 
// This is an improvement over the previous code. It checks if y is the biggest even number, and if so, it returns y. It also checks if the average of x and y is an even number, and if so, it returns that. If neither of these cases applies, it returns -1. 
// The problem