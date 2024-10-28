    vector<int> result;
    int i,j;
    for (i=0;i<x.size();i++)
    {
        int curr_num=x[i];
        bool is_odd=true;
        while (curr_num>0)
        {
            j=curr_num%10;
            if (j%2==0){
                is_odd=false;
                break;
            }
            curr_num/=10;
        }
        if (is_odd==true)
            result.push_back(x[i]);
    }
    sort(result.begin(),result.end());
    return result;
}


