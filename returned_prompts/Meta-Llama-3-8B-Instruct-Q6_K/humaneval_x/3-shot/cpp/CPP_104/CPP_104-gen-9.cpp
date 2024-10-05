    vector<int> result;
    for (int i=0; i<x.size(); i++)
    {
        int num = x[i];
        bool is_valid = true;
        while(num > 0)
        {
            int digit = num % 10;
            if (digit % 2 == 0)
            {
                is_valid = false;
                break;
            }
            num /= 10;
        }
        if (is_valid)
        {
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}
