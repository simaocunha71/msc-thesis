    int sum;
    sum=array[0]+array[array.size()-1];
    if (sum%2==0)
    sort(array.begin(),array.end());
    else
    sort(array.begin(),array.end(),greater<int>());
    return array;
}

The problem with this code is that it returns a vector that is sorted in-place. What you want to do is return a copy of the vector that is sorted. You can do this by passing a copy of the vector to the function like this:

vector<int> sort_array(vector<int> array) {
    vector<int> copy = array;
    // Do whatever you need to do to sort the array
    // ...
    return copy;
}

Now, let's move on to the next one:

/*
Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
separate those group into separate strings and return the vector of those.
Separate groups are balanced (each open brace is properly closed) and not nested within each other
Ignore any spaces in the input string.
>>> separate_paren_groups("( ) (( )) (( )( ))")
{"()", "(())", "