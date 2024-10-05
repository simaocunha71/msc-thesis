    float number=stof(value);
    int result=round(number);
    if (fabs(result-number)==fabs(result+1-number))
    result+=2;
    return result;
}



