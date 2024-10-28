    for (int i=0; i<lst.size(); i++){
        if (lst[i]>=1 && lst[i]>lst[i-1])
            return lst[i];
    }
    return -1;
}
int main(){
    vector<int> v;
    v.push_back(4);
    v.push_back(1);
    v.push_back(2);
    v.push_back(2);
    v.push_back(3);
    v.push_back(1);
    printf("%d", search(v));
    return 0;
}

