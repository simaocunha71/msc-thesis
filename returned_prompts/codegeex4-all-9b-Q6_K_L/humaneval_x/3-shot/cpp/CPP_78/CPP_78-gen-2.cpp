    int i;
    int counter=0;
    for (i=0;i<num.length();i++)
    {
        char chr=num[i];
        if (chr=='2'||chr=='3'||chr=='5'||chr=='7'||chr=='B'||chr=='D')
        counter+=1;
    }
    return counter;
}

