    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        if(lst[i] % 2 == 0){
            continue;
        }
        else{
            sum += lst[i];
        }
    }
    return sum;
}
int main(){
    vector<int> test1{30, 13, 24, 321};
    vector<int> test2{3, 3, 3, 3, 3};
    vector<int> test3{5, 8, 7, 1};
    printf("%d\n", solutions(test3));
}


