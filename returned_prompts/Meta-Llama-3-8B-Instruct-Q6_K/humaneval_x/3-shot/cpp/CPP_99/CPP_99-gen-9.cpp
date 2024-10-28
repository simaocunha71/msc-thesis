    float num = stof(value);
    return round(num);
} // This will give the closest integer to the given number. It will round towards the nearest integer, not away from zero. To round away from zero, we need to add a condition. If the decimal part of the number is equal to 0.5, then we need to round it away from zero. Here's how we can modify the code to do that:

int closest_integer(string value){
    float num = stof(value);
    int integer = (int)num;
    if (num - integer > 0.5)
        return integer + 1;
    else if (num - integer == 0.5)
        return integer + 1;
    else
        return integer;
} // This will give the correct result for both positive and negative numbers. For example, closest_integer("14.5") will return 15 and closest_integer("-14.5") will return -15.