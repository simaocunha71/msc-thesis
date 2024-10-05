    float temp;

    // Ensure c is the longest side
    if(c > a && c > b)
    {
        temp = c;
        c = a;
        a = temp;
    }
    // Ensure b is the longest side
    else if(b > a)
    {
        temp = b;
        b = a;
        a = temp;
    }

    return (a*a == b*b + c*c);
}


