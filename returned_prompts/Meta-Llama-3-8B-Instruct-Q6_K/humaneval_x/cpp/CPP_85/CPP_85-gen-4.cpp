    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        if(i % 2 != 0 && lst[i] % 2 == 0){
            sum += lst[i];
        }
    }
    return sum;
}

int main(){
    vector<int> lst = {4, 2, 6, 7};
    printf("Sum of even elements at odd indices: %d\n", add(lst));
    return 0;
}
