    float number=stof(value);
    float half=truncate_number(number);
    if (number-int(number)>=0.5)
    return (int(number)+1);
    else
    return (int(number));
}


