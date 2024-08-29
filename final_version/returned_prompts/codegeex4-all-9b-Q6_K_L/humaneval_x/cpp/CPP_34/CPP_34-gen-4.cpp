    sort(l.begin(),l.end());    //排序
    vector<int> res;
    int temp;
    int i=0;
    while(i<l.size()-1){
        temp=l[i];
        int j=i+1;
        while(l[j]==temp)
            j++;
        res.push_back(temp);
        i=j;
    }
    res.push_back(l[l.size()-1]);
    return res;
}
int main(){
    vector<int> a;
    a.push_back(5);
    a.push_back(3);
    a.push_back(5);
    a.push_back(2);
    a.push_back(3);
    a.push_back(3);
    a.push_back(9);
    a.push_back(0);
    a.push_back(123);
    vector<int> b=unique(a);
    for(int i=0;i<b.size();i++)
        printf("%d ",b[i]);
    return 0;
}

