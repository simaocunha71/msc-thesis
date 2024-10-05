    float float_value = stof(value);
    int int_value = (int)float_value;
    float decimal = abs(float_value - int_value);
    if (decimal < 0.5)
        return int_value;
    else
        return (float_value < 0) ? int_value : int_value + 1;
}

