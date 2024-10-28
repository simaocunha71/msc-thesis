    int count=0;
    for (auto &chr:s)
    {
        if (chr=='a'||chr=='e'||chr=='i'||chr=='o'||chr=='u'||chr=='A'||chr=='E'||chr=='I'||chr=='O'||chr=='U')
        count+=1;
        if (chr=='y'&&(s.length()-1==i))
        count+=1;
    }
    return count;
}




