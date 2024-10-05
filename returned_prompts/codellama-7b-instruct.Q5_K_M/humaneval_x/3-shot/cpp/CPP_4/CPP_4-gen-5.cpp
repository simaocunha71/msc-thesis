    float sum_abs=0;
    float mean=0;
    float median=0;
    float number;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        number=numbers[i];
        sum_abs+=abs(number-mean);
    }
    return sum_abs/numbers.size();
}


