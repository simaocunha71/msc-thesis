    vector<int> result;
    for (int i=0;i<x.size();i++)
    {
        int temp=x[i];
        bool is_even=false;
        while (temp!=0)
        {
            int digit=temp%10;
            if (digit%2==0)
            {
                is_even=true;
                break;
            }
            temp=temp/10;
        }
        if (!is_even)
            result.push_back(x[i]);
    }
    sort(result.begin(),result.end());
    return result;
} // end of function
// end of class
// end of namespace
// end of program


