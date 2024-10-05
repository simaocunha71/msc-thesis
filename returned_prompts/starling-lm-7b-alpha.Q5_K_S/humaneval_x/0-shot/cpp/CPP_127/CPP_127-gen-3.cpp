    int a = interval1[1]-interval1[0];
    int b = interval2[1]-interval2[0];
    int c = interval2[0]-interval1[1];
    int d = interval1[0]-interval2[1];
    if(a>0&&b>0){
        if(c<0)
            goto A;
        if(c>0&&c<=a)
            return "YES";
    }
    if(a<0&&b<0){
        if(c<0)
            goto A;
        if(c>0&&c<=b)
            return "YES";
    }
    if(a>0&&b<0){
        if(d<0)
            goto A;
        if(d>0&&d<=a)
            return "YES";
    }
    if(a<0&&b>0){
        if(d<0)
            goto A;
        if(d>0&&d<=b)
            return "YES";
    }
    if(a<0&&b<0&&c<0&&d<0)
        return "YES";
    return "NO";
}

int main(){
    vector<int> a,b;
    scanf("%d%d",&a[0],&a[1]);
    scanf("%d%d",&b[0],&b[1]);
    printf("%s\n",intersection(a,b).c_str());
    return 0;
}

















































































































































