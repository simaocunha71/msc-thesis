    if (a<100)
    return false;
    if (a%3==0 || a%5==0 || a%7==0)
    return false;
    if (a%3*5*7==a)
    return true;
    return false;
}


