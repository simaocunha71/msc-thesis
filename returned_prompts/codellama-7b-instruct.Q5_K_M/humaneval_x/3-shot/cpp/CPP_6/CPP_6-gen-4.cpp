    vector<int> max_depth;
    int depth=0;
    int i=0;
    while (i<paren_string.length())
    {
        if (paren_string[i]=='(')
        {
            depth+=1;
        }
        if (paren_string[i]==')')
        {
            depth-=1;
            if (depth>max_depth.back())
            max_depth.push_back(depth);
        }
        i+=1;
    }
    return max_depth;
}


