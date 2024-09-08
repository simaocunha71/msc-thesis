    int max = 0;
    for(int i = 0; i < lst.size(); i++){
        int count = 0;
        for(int j = 0; j < lst.size(); j++){
            if(lst[i] == lst[j]){
                count++;
            }
        }
        if(count >= lst[i] && lst[i] > 0 && lst[i] > max){
            max = lst[i];
        }
    }
    if(max > 0){
        return max;
    } else {
        return -1;
    }
}

int main(){
    vector<int> lst = {4, 1, 2, 2, 3, 1};
    printf("%d\n", search(lst));
    return 0;
}