    if(lst.empty())
    {
        return {0,0};
    }
    int max_negative = INT_MAX;
    int min_positive = INT_MIN;
    for(auto i:lst)
    {
        if(i<0)
        {
            if(i>max_negative)
            {
                max_negative = i;
            }
        }
        else if(i>0)
        {
            if(i<min_positive)
            {
                min_positive = i;
            }
        }
    }
    if(max_negative == INT_MAX)
    {
        return {0,min_positive};
    }
    else if(min_positive == INT_MIN)
    {
        return {max_negative,0};
    }
    return {max_negative,min_positive};
}

int main()
{
    vector<int> lst = {2, 4, 1, 3, 5, 7};
    vector<int> res = largest_smallest_integers(lst);
    cout<<res[0]<<","<<res[1]<<endl;
    return 0;
}
