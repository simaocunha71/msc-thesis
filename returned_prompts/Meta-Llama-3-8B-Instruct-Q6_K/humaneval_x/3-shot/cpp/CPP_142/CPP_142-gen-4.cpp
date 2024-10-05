    int sum=0;
    for(int i=0;i<lst.size();i++)
    {
        if(i%3==0 && i%4!=0)
        {
            sum+=lst[i]*lst[i];
        }
        else if(i%4==0 && i%3!=0)
        {
            sum+=pow(lst[i],3);
        }
        else
        {
            sum+=lst[i];
        }
    }
    return sum;
}  // This function is not very efficient. It can be optimized by iterating over the list only once. 

