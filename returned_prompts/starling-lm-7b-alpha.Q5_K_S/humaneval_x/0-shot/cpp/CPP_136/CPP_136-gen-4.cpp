    vector<int> r;
    for(int i=0;i<lst.size();i++)
    {
        if(lst[i]<0)
        {
            if(r[0]<lst[i])
                r[0]=lst[i];
        }
        else if(lst[i]>0)
        {
            if(r.size()==0)
            {
                r.push_back(lst[i]);
                continue;
            }
            if(r[1]>lst[i])
                r[1]=lst[i];
        }
    }
    if(r.size()==0)
    {
        r.push_back(0);
        r.push_back(0);
    }
    return r;
}


int main()
{
    vector<int> lst={2, 4, 1, 3, 5, 7};
    vector<int> r=largest_smallest_integers(lst);
    for(int i=0;i<r.size();i++)
        printf("%d ",r[i]);
    return 0;
}









































































































































































































































