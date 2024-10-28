    int i;
    int count=0;
    int count2=0;
    string result="";
    for (i=0;i<text.length();i++)
    {
        if (text[i]==' ')
        {
            if (count2==0)
            {
                result=result+"_";
                count2=1;
            }
            else 
            {
                result=result+"-";
                count2=0;
            }
            count++;
        }
        else
        {
            if (count==0)
            {
                result=result+text[i];
            }
            else if (count2==0)
            {
                result=result+"_"+text[i];
                count2=1;
            }
            else 
            {
                result=result+"-"+text[i];
                count2=0;
            }
            count=0;
        }
    }
    return result;
}



