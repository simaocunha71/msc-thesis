    int i=0;
    while (num)
    {
        num&=(num-1);
        i++;
    }
    return i;
}




