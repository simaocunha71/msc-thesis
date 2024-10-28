    int int_part=int(value);
    float dec_part=value-int_part;
    if (int_part==0)
    return int_part;
    else{
        int_part-=1;
        return int_part+1;
    }
}



