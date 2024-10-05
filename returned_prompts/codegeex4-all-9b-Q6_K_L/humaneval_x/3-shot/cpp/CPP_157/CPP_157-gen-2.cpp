    float max_side;
    float sum_of_squares;
    if (a>b&&a>c)
    max_side=a;
    else if (b>a&&b>c)
    max_side=b;
    else if (c>a&&c>b)
    max_side=c;
    sum_of_squares=pow(a,2)+pow(b,2)+pow(c,2);
    if (sum_of_squares==pow(max_side,2))
    return true;
    else
    return false;
}

