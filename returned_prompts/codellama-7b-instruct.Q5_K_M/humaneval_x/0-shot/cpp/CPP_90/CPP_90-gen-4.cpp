    int min_idx = 0;
    int min_value = 10000000;
    for(int i = 0; i < lst.size(); i++){
        if(lst[i] < min_value){
            min_value = lst[i];
            min_idx = i;
        }
    }
    if(lst.size() > 1){
        int tmp = lst[min_idx];
        lst[min_idx] = lst[min_idx + 1];
        lst[min_idx + 1] = tmp;
        goto A;
    }
    return min_value;
}
int main(){
    vector<int> v = {1, 2, 3, 4, 5};
    printf("%d", next_smallest(v));
    return 0;
}
