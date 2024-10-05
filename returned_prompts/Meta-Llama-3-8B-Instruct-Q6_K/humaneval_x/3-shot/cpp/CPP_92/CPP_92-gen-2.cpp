    if (a==int(a) && b==int(b) && c==int(c))
    {
        if (a==b+c || b==a+c || c==a+b)
        return true;
    }
    return false;
}  // Note: You can also use a single line of code to solve this problem. bool any_int(float a, float b, float c) { return (a==int(a) && b==int(b) && c==int(c)) && (a==b+c || b==a+c || c==a+b); }