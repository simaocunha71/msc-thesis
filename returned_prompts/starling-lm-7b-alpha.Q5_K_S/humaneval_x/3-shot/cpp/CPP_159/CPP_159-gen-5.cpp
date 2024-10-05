    int eaten = number+need;
    int left = remaining-need;
    if (left<0)
    {
        eaten+=left;
        left=0;
    }
    return vector<int>({eaten,left});
}



