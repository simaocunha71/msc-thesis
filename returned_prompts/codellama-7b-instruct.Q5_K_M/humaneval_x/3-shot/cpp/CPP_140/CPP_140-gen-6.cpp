    string temp="";
    int length=text.length();
    int i;
    for (i=0;i<length;i++)
    {
        if (text[i]==' ')
        {
            if (i==length-1)
            {
                temp+="_";
            }
            else if (text[i+1]==' ')
            {
                temp+="-";
                i++;
            }
            else
            {
                temp+="_";
            }
        }
        else
        {
            temp+=text[i];
        }
    }
    return temp;
}





