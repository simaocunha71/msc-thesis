    float number = stof(value);
    int int_part = (int)number;
    float decimal_part = abs(number - int_part);

    if (decimal_part < 0.5)
        return int_part;
    else if (number > 0)
        return int_part + 1;
    else 
        return int_part - 1;
}


