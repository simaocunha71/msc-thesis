    double num = stod(value);
    int integer = (int)round(num);
    if(num - integer >= 0.5) return integer + 1;
    else return integer;
}

