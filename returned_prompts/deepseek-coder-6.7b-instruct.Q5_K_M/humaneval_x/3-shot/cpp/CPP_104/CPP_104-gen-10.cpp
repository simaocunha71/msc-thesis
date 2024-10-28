    vector<int> result;
    int i;
    for  (i=0; i<x.size(); i++)
    {
        int num = x[i];
        bool flag = false;
        while  (num > 0 && !flag)
        {
            int digit = num % 10;
            if  (digit % 2 == 0)
            {
                flag = true;
                break;
            }
            num = num / 10;
        }
        if  (!flag)
        {
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

