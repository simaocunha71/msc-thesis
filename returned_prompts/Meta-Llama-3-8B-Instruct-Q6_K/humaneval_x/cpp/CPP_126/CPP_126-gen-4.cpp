    if(lst.size() <= 1)
        return true;
    for(int i=0; i<lst.size()-1; i++){
        if(lst[i] >= lst[i+1]){
            if(i+1 < lst.size()-1 && lst[i] == lst[i+1])
                return false;
        }
        else
            return false;
    }
    return true;
}
int main(){
    vector<int> v1={5};
    vector<int> v2={1, 2, 3, 4, 5};
    vector<int> v3={1, 3, 2, 4, 5};
    vector<int> v4={1, 2, 3, 4, 5, 6};
    vector<int> v5={1, 2, 3, 4, 5, 6, 7};
    vector<int> v6={1, 3, 2, 4, 5, 6, 7};
    vector<int> v7={1, 2, 2, 3, 3, 4};
    vector<int> v8={1, 2, 2, 2, 3, 4};
    printf("is_sorted(%d) ➞ %d\n", sizeof(v1)/sizeof(v1[0]), is_sorted(v1));
    printf("is_sorted(%d) ➞ %d\n", sizeof(v2)/sizeof(v2[0]), is_sorted(v2));
    printf("is_sorted(%d) ➞ %d\n", sizeof(v3)/sizeof(v3[0]), is_sorted(v3));
    printf("is_sorted(%d) ➞ %d\n", sizeof(v4)/sizeof(v4[0]), is_sorted(v4));
    printf("is_sorted(%d) ➞ %d\n", sizeof(v5)/sizeof(v5[0]), is_sorted(v5));
    printf("is_sorted(%d) ➞ %d\n", sizeof(v6)/sizeof(v6[0]), is_sorted(v6));
    printf("is_sorted(%d) ➞ %d\n", sizeof(v7)/sizeof(v7[0]), is_sorted(v7));
    printf("is_sorted(%d) ➞ %d\n", sizeof(v8)/sizeof(v8[0]), is_sorted(v8));
    return 0;
}

