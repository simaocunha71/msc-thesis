    vector<int> result;
    for (int i=0;i<x.size();i++)
    {
        int num=x[i];
        bool has_even_digit=0;
        while (num>0)
        {
            if (num%10==2||num%10==4||num%10==6||num%10==8)
            {
                has_even_digit=1;
                break;
            }
            num=num/10;
        }
        if (!has_even_digit)
            result.push_back(x[i]);
    }
    sort(result.begin(),result.end());
    return result;
}
//OR
vector<int> unique_digits(vector<int> x){
    vector<int> result;
    for (int i=0;i<x.size();i++)
    {
        int num=x[i];
        bool has_even_digit=0;
        while (num>0)
        {
            if (num%10==2||num%10==4||num%10==6||num%10==8)
            {
                has_even_digit=1;
                break;
            }
            num=num/10;
        }
        if (!has_even_digit)
            result.push_back(x[i]);
    }
    sort(result.begin(),result.end());
    return result;
}
//OR
vector<int> unique_digits(vector<int> x){
    vector<int> result;
    for (int i=0;i<x.size();i++)
    {
        int num=x[i];
        bool has_even_digit=0;
        while (num>0)
        {
            if (num%10==2||num%10==4||num%10==6||num%10==8)
            {
                has_even_digit=1;
                break;
            }
            num=num/10;
        }
        if (!has_even_digit)
            result.push_back(x[i]);
    }
    sort(result.begin(),result.end());
    return result;
} //OR
vector<int> unique_digits(vector<int> x){
    vector<int> result;
    for (int i=0;i<x.size();i++)
    {
        int num=x[i];
        bool has_even_digit=0;
        while (num>0)
        {
            if (num%10==2||num%10==4||num%10==6||num%10==8)
            {
                has_even_digit=1;
                break;
            }
            num=num/10;
        }
        if (!has_even_digit)
            result.push_back(x[i]);
