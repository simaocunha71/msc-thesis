    int start1=interval1[0],end1=interval1[1];
    int start2=interval2[0],end2=interval2[1];
    if (end1<start2 || end2<start1) return "NO";
    int start=max(start1,start2);
    int end=min(end1,end2);
    int length=end-start;
    if (length<=0) return "NO";
    if (length==1) return "NO";
    if (length==2 && start1==start2) return "NO";
    int prime=1;
    for (int i=2;i<=length;i++)
    if (length%i==0) prime=0;
    if (prime==1) return "YES";
    else return "NO";
}


