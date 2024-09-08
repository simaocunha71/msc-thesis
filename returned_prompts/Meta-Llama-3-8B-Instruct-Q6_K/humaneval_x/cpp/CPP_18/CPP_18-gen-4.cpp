    int count=0;
    int pos=0;
    while((pos=str.find(substring,pos))!=string::npos){
        count++;
        pos=pos+1;
    }
    return count;
}
