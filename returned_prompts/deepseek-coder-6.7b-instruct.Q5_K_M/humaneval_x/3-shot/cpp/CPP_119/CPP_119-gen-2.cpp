    int count = 0;
    for(auto str : lst)
        for(auto c : str)
            if(c == '(')
                count++;
            else if(c == ')')
                count--;
            if(count < 0)
                return "No";
    return count == 0 ? "Yes" : "No";
}

