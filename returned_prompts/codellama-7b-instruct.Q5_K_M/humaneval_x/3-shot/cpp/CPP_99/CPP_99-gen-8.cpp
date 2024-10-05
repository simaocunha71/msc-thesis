    float num=stof(value);
    int int_part=int(num);
    float dec_part=num-int_part;
    if (dec_part==0)
    return int_part;
    if (dec_part>0.5)
    return int_part+1;
    return int_part-1;
}


