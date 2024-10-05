    string roman;
    int temp;
    while (number>0)
    {
        if (number>=1000)
        {
            temp=number/1000;
            number=number%1000;
            for (int i=0;i<temp;i++)
                roman+="m";
        }
        else if (number>=900)
        {
            temp=number/900;
            number=number%900;
            for (int i=0;i<temp;i++)
                roman+="cm";
        }
        else if (number>=500)
        {
            temp=number/500;
            number=number%500;
            for (int i=0;i<temp;i++)
                roman+="d";
        }
        else if (number>=400)
        {
            temp=number/400;
            number=number%400;
            for (int i=0;i<temp;i++)
                roman+="cd";
        }
        else if (number>=100)
        {
            temp=number/100;
            number=number%100;
            for (int i=0;i<temp;i++)
                roman+="c";
        }
        else if (number>=90)
        {
            temp=number/90;
            number=number%90;
            for (int i=0;i<temp;i++)
                roman+="xc";
        }
        else if (number>=50)
        {
            temp=number/50;
            number=number%50;
            for (int i=0;i<temp;i++)
                roman+="l";
        }
        else if (number>=40)
        {
            temp=number/40;
            number=number%40;
            for (int i=0;i<temp;i++)
                roman+="xl";
        }
        else if (number>=10)
        {
            temp=number/10;
            number=number%10;
            for (int i=0;i<temp;i++)
                roman+="x";
        }
        else if (number>=9)
        {
            temp=number/9;
            number=number%9;
            for (int i=0;i<temp;i++)
                roman+="ix";
        }
        else if (number>=5)
        {
            temp=number/5;
            number=number%5;
            for (int i=0;i<temp;i++)
                roman+="v";
        }
        else if (number>=4)
        {
            temp=number/4;
            number=