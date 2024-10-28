    float num = stof(value);
    if (num - int(num) < 0.5)
        return int(num);
    else
        return int(num) + 1;
}  //  This function will round the number away from zero. If the number is equidistant from two integers, it will round it away from zero.