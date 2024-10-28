    if (a+b>c && b+c>a && a+c>b)
    return roundf(sqrt(pow((a*b),2)-(pow((a-b),2)*pow((c-a),2))))*100.0/100.0;
    else
    return -1;
}


