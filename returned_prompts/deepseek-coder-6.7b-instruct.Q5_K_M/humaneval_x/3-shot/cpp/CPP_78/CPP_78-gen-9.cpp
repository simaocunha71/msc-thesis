    int count=0;
    string hex="2357BDF";
    for(auto i:num)
    {
        if(hex.find(i)!=string::npos)
        count++;
    }
    return count;
}

