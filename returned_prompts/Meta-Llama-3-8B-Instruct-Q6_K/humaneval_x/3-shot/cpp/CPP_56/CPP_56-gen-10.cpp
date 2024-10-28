    int i,j;
    stack<char> s;
    for (i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='<')
            s.push('<');
        else if (brackets[i]=='>')
        {
            if (s.empty())
                return false;
            s.pop();
        }
    }
    return s.empty();
} // end of function correct_bracketing


