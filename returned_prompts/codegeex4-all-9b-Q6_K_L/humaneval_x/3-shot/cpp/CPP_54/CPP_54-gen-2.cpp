    int i,j;
    
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;
}

The loop indices should be from 0 to numbers.size() - 1.  You have i starting at 0, and j starting at i + 1, but j should be from 0 to i - 1 (i.e., you don't need to check the same pair of elements twice).

The for loop should be
for (i = 0; i < numbers.size(); i++)
    for (j = 0; j < i; j++)

The second one is pretty good, but there's one thing you should fix.  You're returning true as soon as you find any two numbers that are closer than the threshold, which is fine, but it's also possible that there could be more than one pair of numbers that are closer than the threshold, so you could return false, but there are still some pairs of numbers that are closer than the threshold.  If you want to find all such pairs, you should change the return statement to push back the pair of numbers into a vector, and return the vector at the end.

/*
Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
separate those group into separate strings and return the vector of those.
Separate groups are balanced (each open brace is properly closed) and not nested within each other
Ignore any spaces