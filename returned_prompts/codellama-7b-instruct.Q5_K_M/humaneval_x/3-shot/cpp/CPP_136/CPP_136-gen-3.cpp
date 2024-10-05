    int largest_negative=0;
    int smallest_positive=0;
    for (int i=0;i<lst.size();i++)
    {
        if (lst[i]<0)
        {
            if (lst[i]>largest_negative)
            largest_negative=lst[i];
        }
        if (lst[i]>0)
        {
            if (lst[i]<smallest_positive)
            smallest_positive=lst[i];
        }
    }
    vector<int> final_ans;
    final_ans.push_back(largest_negative);
    final_ans.push_back(smallest_positive);
    return final_ans;
}

