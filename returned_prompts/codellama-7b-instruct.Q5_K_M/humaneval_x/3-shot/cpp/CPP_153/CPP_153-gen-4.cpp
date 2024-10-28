    int cap_counter,sm_counter,max_cap,max_sm;
    int i,j;
    for (i=0;i<extensions.size();i++)
    {
        cap_counter=0;
        sm_counter=0;
        for (j=0;j<extensions[i].length();j++)
        {
            if (isupper(extensions[i][j]))
            {
                cap_counter++;
            }
            if (islower(extensions[i][j]))
            {
                sm_counter++;
            }
        }
        if (i==0)
        {
            max_cap=cap_counter;
            max_sm=sm_counter;
        }
        if (cap_counter-sm_counter>max_cap-max_sm)
        {
            max_cap=cap_counter;
            max_sm=sm_counter;
        }
    }
    return class_name+"."+extensions[i];
}


