    if (a<b)
    return greatest_common_divisor(b, a);
    if (b==0)
    return a;
    return greatest_common_divisor(b, a%b);
}


