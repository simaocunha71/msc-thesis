    float l_size=l.size();
    float i;
    float j;
    float first_i=l[0];
    float second_i=l[1];
    float last_i=l[l_size-1];
    float second_last_i=l[l_size-2];
    float last_last_i=l[l_size-3];
    float first_last_i=l[1];
    float first_last=l[1]-l[0];
    float second_last_last=l[2]-l[1];
    float last_second_last=l[l_size-2]-l[l_size-3];
    float last_last=l[l_size-1]-l[l_size-2];
    float first_last_last=l[l_size-1]-l[l_size-3];
    float last_last_last=l[l_size-1]-l[l_size-2];
    float last_last_last_last=l[l_size-2]-l[l_size-3];
    
    for (i=0;i<l.size();i++)
    {
        for (j=i+1;j<l.size();j++)
        {
            if (first_last<second_last_last)
            {
                return false;
            }
            if (first_last>second_last_last)
            {
                return true;
            }
        }
    }
    
    
}




