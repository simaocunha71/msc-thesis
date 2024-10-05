    int eaten=need-number;
    if (eaten>remaining)
    {
        eaten=remaining;
        remaining=0;
    }
    else
    {
        remaining-=eaten;
        eaten+=number;
    }
    return vector<int> {eaten,remaining};
}



