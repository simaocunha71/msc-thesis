    int i,j;
    
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;
}

The first thing I notice is that you've included math.h, but you are using the abs() function from the standard library. You can remove the math.h include, and simply use:
#include <cmath>

Next, you've used the preprocessor directive #include<stdio.h> to include the standard input/output library. You don't actually need this, because none of your code uses it. It is safe to remove it. 
You've also used the preprocessor directive #include<vector> to include the standard vector library. This is a good idea, because you are using it in your code. It is safe to keep this include. 
You've also used the preprocessor directive #include<math.h> to include the standard math library. This is a good idea, because you are using it in your code. It is safe to keep this include. 

/*
Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
separate those group into separate strings and return the vector of those.
Separate groups are balanced (each open brace is properly closed) and not nested within each other
Ignore any spaces in the input string.
>>> separate_paren