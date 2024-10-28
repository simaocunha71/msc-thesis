    int i,j;
    int max_element=-1;
    int max_frequency=-1;
    for (i=0;i<lst.size();i++)
    {
        int current_element=lst[i];
        int current_frequency=0;
        for (j=0;j<lst.size();j++)
        {
            if (current_element==lst[j])
            {
            current_frequency+=1;
            }
        }
        if (current_frequency>current_element && current_frequency>max_frequency){
        max_element=current_element;
        max_frequency=current_frequency;
        }
    }
    return max_element;
}



