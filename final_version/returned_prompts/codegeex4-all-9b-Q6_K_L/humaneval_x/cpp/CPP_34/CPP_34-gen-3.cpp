    sort(l.begin(),l.end());
    vector<int> v;
    for(int i=0;i<l.size();i++){
        if(i==0){
            v.push_back(l[i]);
        }
        else{
            if(l[i]!=l[i-1]){
                v.push_back(l[i]);
            }
        }
    }
    return v;
}
int main(){
    vector<int> a={5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> b=unique(a);
    for(int i=0;i<b.size();i++){
        printf("%d ",b[i]);
    }
    return 0;
}
