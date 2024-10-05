    int i,j;
    int max_index=-1;
    int max_strength=-1;
    for (i=0;i<extensions.size();i++)
    {
        int cap_count=0;
        int sm_count=0;
        for (j=0;j<extensions[i].length();j++)
        {
            if ('A'<=extensions[i][j] && extensions[i][j]<='Z')
            cap_count+=1;
            else if ('a'<=extensions[i][j] && extensions[i][j]<='z')
            sm_count+=1;
        }
        int strength=cap_count-sm_count;
        if (strength>max_strength){
        max_strength=strength;
        max_index=i;
        }
    }
    return class_name+". "+extensions[max_index];
}


