    string binary;
    int i;
    for (i=0;i<32;i++)
    if (decimal%2==0)
    binary+="0";
    else
    binary+="1";
    binary="db"+binary+"db";
    return binary;
}

What you have here is basically 4 functions that work on different data types.  The first function takes in a vector of floats and a float and returns a boolean.  The second function takes in a string of characters and returns a vector of strings.  The third function takes in a float and returns a float.  The fourth function takes in an integer and returns a string.  This is good, but you can make a few improvements.  First, you should add a comment at the top of your file explaining what the file is for.  This will help anyone reading your code understand what it does.  Next, you should add comments for each function explaining what the function does, what parameters