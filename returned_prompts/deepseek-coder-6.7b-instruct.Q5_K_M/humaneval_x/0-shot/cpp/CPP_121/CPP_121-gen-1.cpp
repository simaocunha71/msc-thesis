    int sum=0;
    for(int i=0;i<lst.size();i+=2){
        if(lst[i]%2 != 0) sum+= lst[i];
    }
    return sum;
}

int main(){
    vector<int> test1 = {5, 8, 7, 1};
    vector<int> test2 = {3, 3, 3, 3, 3};
    vector<int> test3 = {30, 13, 24, 321};
    
    printf("%d\n", solutions(test1)); // 12
    printf("%d\n", solutions(test2)); // 9
    printf("%d\n", solutions(test3)); // 0
}


