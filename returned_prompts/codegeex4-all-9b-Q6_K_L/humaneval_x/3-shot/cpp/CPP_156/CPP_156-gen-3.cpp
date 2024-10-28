    string roman="";
    int i;
    int num_copy=number;
    for (i=0;i<num_copy;i++)
    {
        if (num_copy>=1000)
        {
            roman+='m';
            num_copy-=1000;
        }
        else if (num_copy>=900)
        {
            roman+='c';
            roman+='m';
            num_copy-=900;
        }
        else if (num_copy>=500)
        {
            roman+='d';
            num_copy-=500;
        }
        else if (num_copy>=400)
        {
            roman+='c';
            roman+='d';
            num_copy-=400;
        }
        else if (num_copy>=100)
        {
            roman+='c';
            num_copy-=100;
        }
        else if (num_copy>=90)
        {
            roman+='x';
            roman+='c';
            num_copy-=90;
        }
        else if (num_copy>=50)
        {
            roman+='l';
            num_copy-=50;
        }
        else if (num_copy>=40)
        {
            roman+='x';
            roman+='l';
            num_copy-=40;
        }
        else if (num_copy>=10)
        {
            roman+='x';
            num_copy-=10;
        }
        else if (num_copy>=9)
        {
            roman+='ix';
            num_copy-=9;
        }
        else if (num_copy>=5)
        {
            roman+='v';
            num_copy-=5;
        }
        else if (num_copy>=4)
        {
            roman+='iv';
            num_copy-=4;
        }
        else if (num_copy>=1)
        {
            roman+='i';
            num_copy-=1;
        }
    }
    return roman;
}

