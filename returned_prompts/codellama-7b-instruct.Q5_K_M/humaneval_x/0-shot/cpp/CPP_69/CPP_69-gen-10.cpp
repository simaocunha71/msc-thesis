    int freq = 0;
    for (int i = 0; i < lst.size(); i++)
    {
        if (lst[i] == 1)
            freq++;
    }
    if (freq >= 1)
        return 1;
    else if (freq == 0)
    {
        for (int i = 0; i < lst.size(); i++)
        {
            if (lst[i] > 1)
                freq++;
        }
        if (freq >= 2)
            return 2;
    }
    else
    {
        for (int i = 0; i < lst.size(); i++)
        {
            if (lst[i] > 2)
                freq++;
        }
        if (freq >= 3)
            return 3;
    }
    return -1;
}

int main()
{
    vector<int> lst = { 4, 1, 2, 2, 3, 1 };
    printf("%d\n", search(lst));
    return 0;
}

