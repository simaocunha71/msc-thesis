    vector<int> result;
    int i,j;
    for (i=0;i<x.size();i++)
    {
        bool is_even_digit=false;
        for (j=0;j<x[i];j++)
        {
            if (x[i]%10==j%2){
                is_even_digit=true;
                break;
            }
            x[i]/=10;
        }

        if (!is_even_digit)
        {
            result.push_back(x[i]);
        }
    }

    sort(result.begin(),result.end());
    return result;
}




