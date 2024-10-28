    vector<int> v;
    sort(l1.begin(),l1.end());
    sort(l2.begin(),l2.end());
    vector<int>::iterator it;
    int i=0,j=0;
    while(i<l1.size()&&j<l2.size()){
        if(l1[i]==l2[j]){
            v.push_back(l1[i]);
            i++;
            j++;
        }else if(l1[i]<l2[j]){
            i++;
        }else{
            j++;
        }
    }
    return v;
}
int main(){
    vector<int> a={1, 4, 3, 34, 653, 2, 5};
    vector<int> b={5, 7, 1, 5, 9, 653, 121};
    vector<int> c={5, 3, 2, 8};
    vector<int> d={3, 2};
    vector<int> v,w;
    v=common(a,b);
    w=common(c,d);
    printf("Result of common({1, 4, 3, 34, 653, 2, 5}, {5, 7, 1, 5, 9, 653, 121}) is: ");
    for(int i=0;i<v.size();i++){
        printf("%d, ",v[i]);
    }
    printf("\n");
    printf("Result of common({5, 3, 2, 8}, {3, 2}) is: ");
    for(int i=0;i<w.size();i++){
        printf("%d, ",w[i]);
    }
    printf("\n");
    return 0;
}


























































