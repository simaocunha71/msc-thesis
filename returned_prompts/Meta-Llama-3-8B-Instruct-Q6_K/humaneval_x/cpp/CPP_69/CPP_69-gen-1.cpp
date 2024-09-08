    int max = 0;
    int count = 0;
    for(int i = 1; i <= *max_element(lst.begin(), lst.end()); i++){
        count = 0;
        for(int j = 0; j < lst.size(); j++){
            if(lst[j] == i){
                count++;
            }
        }
        if(count >= i){
            max = i;
        }
    }
    if(max == 0){
        return -1;
    }else{
        return max;
    }
}
int main(){
    vector<int> lst = {4, 1, 2, 2, 3, 1};
    printf("%d\n", search(lst));
    return 0;
}
