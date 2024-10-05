    sort(lst.begin(),lst.end(),[](int a,int b){
        return abs(a)==abs(b)?a>b:abs(a)<abs(b);
    });
    return lst;
}

