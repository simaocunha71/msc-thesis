    int i,count;
    map<char,int> result;
    char chr;
    for (i=0;i<test.length();i++)
    {
        chr=test[i];
        if (result[chr]==0)
        {
            count=1;
            result[chr]=count;
        }
        else
        {
            count=result[chr]+1;
            result[chr]=count;
        }
    }

    return result;
}



