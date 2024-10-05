    string mini_roman;
    if (number==1000)
    return "m";
    if (number>=500)
    {
        mini_roman="d";
        number-=500;
    }
    if (number>=100)
    {
        mini_roman+="c";
        number-=100;
    }
    if (number>=50)
    {
        mini_roman+="l";
        number-=50;
    }
    if (number>=10)
    {
        mini_roman+="x";
        number-=10;
    }
    if (number>=5)
    {
        mini_roman+="v";
        number-=5;
    }
    if (number>=1)
    {
        mini_roman+="i";
        number-=1;
    }
    return mini_roman;
}

