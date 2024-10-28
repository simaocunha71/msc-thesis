    int i,j,max=-256,count;
    string strong_ext="";
    char chr;
    for(i=0;i<extensions.size();i++)
    {
        count=0;
        for(j=0;j<extensions[i].length();j++)
        {
            chr=extensions[i][j];
            if(isupper(chr))
            count++;
            else if(islower(chr))
            count--;
        }
        if(count>max)
        {
            max=count;
            strong_ext=extensions[i];
        }
    }
    return class_name+"."+strong_ext;
}




