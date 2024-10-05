    if (a+b<=c||a+c<=b||b+c<=a)
    return -1;

    return sqrt((a+b+c)*(a+b-c)*(a+c-b)*(b+c-a))/4;
}