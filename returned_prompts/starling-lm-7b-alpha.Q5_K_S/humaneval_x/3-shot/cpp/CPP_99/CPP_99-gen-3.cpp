    int i;
    int result;
    float number=stof(value);
    float temp;
    for (i=0;i<value.length();i++)
    if (value[i]=='.')
    break;
    temp=stof(value.substr(0,i));
    if (number-temp==0.5)
    result=temp+1;
    else if (number-temp==0.0)
    result=temp-1;
    else if ((number-temp)<0.5)
    result=temp;
    else
    result=temp+1;
    return result;
}




