    int j=lst.size()-1;
    int k=0;
    bool flag=true;
    for(int i=0;i<lst.size()-1;i++){
        if(lst[i]>lst[i+1]){
            flag=false;
        }
        if(lst[i]==lst[i+1]){
            j=i;
            k++;
        }
    }
    if(k>1 || !flag){
        return false;
    }
    else{
        return true;
    }
}

int main(){
    vector<int> lst;
    lst={1, 3, 2, 4, 5, 6, 7};
    cout<<is_sorted(lst)<<endl;
    return 0;
}

Ans: C
bool is_sorted(vector<int> lst) {
    if (lst.size() < 2) return true;
    for (int i = 0; i < lst.size() - 1; i++) {
        if (lst[i] > lst[i + 1]) {
            return false;
        }
    }
    return true;
}

