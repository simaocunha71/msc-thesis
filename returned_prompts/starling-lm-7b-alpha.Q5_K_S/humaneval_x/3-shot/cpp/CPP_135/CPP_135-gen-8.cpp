    int i,j,max_index;
    max_index=-1;
    for (i=0;i<arr.size();i++)
    {
        for (j=0;j<i;j++)
        {
            if (arr[i]<arr[j])
            {
                if (max_index==-1||i>max_index){
                    max_index=i;
                }
            }
        }
    }
    return max_index;
}


