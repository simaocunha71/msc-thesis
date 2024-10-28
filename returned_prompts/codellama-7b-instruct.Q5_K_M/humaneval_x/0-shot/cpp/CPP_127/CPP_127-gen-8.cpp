    int start1=interval1[0];
    int end1=interval1[1];
    int start2=interval2[0];
    int end2=interval2[1];
    if(start1>end2||end1<start2)
        return "NO";
    int start=max(start1,start2);
    int end=min(end1,end2);
    if(end-start<=0)
        return "NO";
    int length=end-start+1;
    bool flag=true;
    for(int i=2;i<=length;++i)
        if(length%i==0)
            flag=false;
    if(flag)
        return "YES";
    return "NO";
}
int main()
{
    vector<int> a1={-3, -1};
    vector<int> a2={-5, 5};
    printf("%s",intersection(a1,a2).c_str());
    return 0;
}
