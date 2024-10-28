    if (lst.size()==0) return None;
    if (lst.size()==1) return None;
    if (lst.size()==2) return lst[1];
    if (lst.size()>2) {
        sort(lst.begin(),lst.end());
        int i=0;
        for(i=0; i<lst.size()-1; i++){
            if (lst[i]<lst[i+1]){
                return lst[i+1];
            }
        }
    }
}
int main(){
    vector<int> lst;
    int a;
    while(scanf("%d",&a)!=EOF){
        lst.push_back(a);
    }
    int ans=next_smallest(lst);
    if (ans==None) printf("None\n");
    else printf("%d\n",ans);
    return 0;
}
