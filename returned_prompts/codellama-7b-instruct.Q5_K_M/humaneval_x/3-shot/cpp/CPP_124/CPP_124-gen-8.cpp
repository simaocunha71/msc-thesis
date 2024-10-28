    int len=date.length();
    if (len==0)
    return false;
    if (date[2]=='/'||date[2]=='-')
    return false;
    if (date[0]<'1'||date[0]>'3')
    return false;
    if (date[1]<'1'||date[1]>'2')
    return false;
    if (date[3]<'0'||date[3]>'9')
    return false;
    if (date[5]<'0'||date[5]>'9')
    return false;
    if (date[7]<'0'||date[7]>'9')
    return false;
    if (date[8]<'0'||date[8]>'9')
    return false;
    if (date[9]<'0'||date[9]>'9')
    return false;
    if (date[10]<'0'||date[10]>'9')
    return false;
    if (date[11]<'0'||date[11]>'9')
    return false;
    if (date[12]<'0'||date[12]>'9')
    return false;
    if (date[13]<'0'||date[13]>'9')
    return false;
    return true;
}




