    int i,j;
    
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;
}

The algorithm is fine, but you can simplify the loop by removing the j=i+1.  Also, your comments are a bit off.  The example you gave for false is actually true, since 2.0 and 2.8 are closer than the threshold of 0.5.
Here is the updated code:
/*
Check if in given vector of numbers, are any two numbers closer to each other than
given threshold.
>>> has_close