    int month,day,year;
    sscanf(date.c_str(),"%d-%d-%d",&month,&day,&year);
    if (month>=1 && month<=12 && day>=1 && day<=31 && year>=1)
    return true;
    else
    return false;
}

