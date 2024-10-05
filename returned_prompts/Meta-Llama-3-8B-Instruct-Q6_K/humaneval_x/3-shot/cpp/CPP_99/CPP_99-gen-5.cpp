    float num=atof(value.c_str());
    int integer_part = int(num);
    if (abs(num-integer_part) > 0.5)
        return integer_part+1;
    else
        return integer_part;
}

