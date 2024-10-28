    float number;
    sscanf(value.c_str(), "%f", &number);
    if (number>=0)
    return (int)ceil(number);
    else
    return (int)floor(number);
}


