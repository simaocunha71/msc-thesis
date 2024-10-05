    int i,upper_count,lower_count,max_strength=-1000,index=0;
    for(i=0;i<extensions.size();i++)
    {
        upper_count=0,lower_count=0;
        for(char & c : extensions[i])
        {
            if(isupper(c))
            upper_count++;
            if(islower(c))
            lower_count++;
        }
        if((upper_count-lower_count)>max_strength)
        {
            max_strength=upper_count-lower_count;
            index=i;
        }
    }
    return class_name+'.'+extensions[index];
}


