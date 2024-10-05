    int i,max_strength=-1,max_index=-1;
    for (i=0;i<extensions.size();i++)
    {
        int strength=0;
        int j;
        for (j=0;j<extensions[i].length();j++)
        {
            if (extensions[i][j]>='A'&&extensions[i][j]<='Z')
                strength+=1;
            if (extensions[i][j]>='a'&&extensions[i][j]<='z')
                strength-=1;
        }
        if (strength>=max_strength){
            max_strength=strength;
            max_index=i;
        }
    }
    return class_name+". "+extensions[max_index];
}




