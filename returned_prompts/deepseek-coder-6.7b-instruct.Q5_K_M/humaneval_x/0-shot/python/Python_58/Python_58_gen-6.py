    sort(l.begin(),l.end());
    for  (int i = 0; i < l.size() - 2; i++)
    {
        int j = i + 1, k = l.size() - 1;
        while  (j < k)
        {
            if  ((l[i] + l[j] + l[k]) == 0)
            {
                return true;
            }
            else if  ((l[i] + l[j] + l[k]) < 0)
            {
                j += 1;
            }
            else
            {
                k -= 1;
            }
        }
    }
    return false;
}



