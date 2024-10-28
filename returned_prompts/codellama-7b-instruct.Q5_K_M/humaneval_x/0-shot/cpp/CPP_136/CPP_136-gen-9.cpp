    int a = 0, b = 0;
    for(int i = 0; i < lst.size(); i++){
        if(lst[i] < 0 && a < lst[i]){
            a = lst[i];
        }
        else if(lst[i] > 0 && b > lst[i]){
            b = lst[i];
        }
    }
    if(a == 0 && b == 0){
        a = 0;
        b = 0;
    }
    vector<int> vec {a, b};
    return vec;
}
int main(){
    vector<int> lst {2, 4, 1, 3, 5, 7};
    vector<int> result = largest_smallest_integers(lst);
    for(int i = 0; i < 2; i++){
        printf("result[%d] = %d\n", i, result[i]);
    }
    return 0;
}
