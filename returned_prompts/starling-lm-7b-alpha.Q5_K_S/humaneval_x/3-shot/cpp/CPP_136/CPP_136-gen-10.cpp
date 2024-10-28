    int i;
    int neg_num=-1000000000;
    int pos_num=1000000000;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]<0 && lst[i]>neg_num)
        {
        neg_num=lst[i];
        }
        if (lst[i]>0 && lst[i]<pos_num)
        {
        pos_num=lst[i];
        }
    }
    vector<int> res={neg_num,pos_num};
    return res;
}




