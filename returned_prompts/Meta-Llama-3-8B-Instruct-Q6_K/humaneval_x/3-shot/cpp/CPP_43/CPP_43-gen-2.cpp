    set<int> s;
    for (int i : l)
    {
        if (s.find(-i)!=s.end())
        return true;
        s.insert(i);
    }
    return false;
} // end of pairs_sum_to_zero function
// end of code

