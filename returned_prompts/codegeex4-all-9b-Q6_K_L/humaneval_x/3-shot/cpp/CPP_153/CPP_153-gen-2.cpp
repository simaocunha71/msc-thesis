    int i,j;
    int max=-1000;
    string max_string;
    for (i=0;i<extensions.size();i++)
    {
        int count=0;
        int count2=0;
        for (j=0;j<extensions[i].length();j++)
        {
            if (isupper(extensions[i][j]))
                count++;
            else
                count2++;
        }
        if (count-count2>max){
            max_string=extensions[i];
            max=count-count2;
        }
    }
    return class_name+'.'+max_string;
}

