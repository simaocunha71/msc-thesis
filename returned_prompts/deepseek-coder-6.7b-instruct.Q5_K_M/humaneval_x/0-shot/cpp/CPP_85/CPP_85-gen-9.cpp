    int sum = 0;
    for(int i = 1; i < lst.size(); i += 2){
        if(lst[i] % 2 == 0){
            sum += lst[i];
        }
    }
    return sum;
}
int main(){
    vector<int> lst = {4, 2, 6, 7};
    printf("%d", add(lst));
    return 0;
}

