    float num;
    num=stof(value);
    if (num-int(num)>=0.5)
    return int(num)+1;
    else
    return int(num);
}

