    string roman_num="";
    while (number>=1000)
    {
        roman_num+="m";
        number-=1000;
    }
    while (number>=900)
    {
        roman_num+="cm";
        number-=900;
    }
    while (number>=500)
    {
        roman_num+="d";
        number-=500;
    }
    while (number>=400)
    {
        roman_num+="cd";
        number-=400;
    }
    while (number>=100)
    {
        roman_num+="c";
        number-=100;
    }
    while (number>=90)
    {
        roman_num+="xc";
        number-=90;
    }
    while (number>=50)
    {
        roman_num+="l";
        number-=50;
    }
    while (number>=40)
    {
        roman_num+="xl";
        number-=40;
    }
    while (number>=10)
    {
        roman_num+="x";
        number-=10;
    }
    while (number>=9)
    {
        roman_num+="ix";
        number-=9;
    }
    while (number>=5)
    {
        roman_num+="v";
        number-=5;
    }
    while (number>=4)
    {
        roman_num+="iv";
        number-=4;
    }
    while (number>=1)
    {
        roman_num+="i";
        number-=1;
    }
    return roman_num;
}

