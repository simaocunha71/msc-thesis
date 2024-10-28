    float number=stof(value);
    float integer=round(number);
    float integer_next=integer+1;
    if (abs(integer-number)<abs(integer_next-number))
    return (int)integer;
    else
    return (int)integer_next;
}


