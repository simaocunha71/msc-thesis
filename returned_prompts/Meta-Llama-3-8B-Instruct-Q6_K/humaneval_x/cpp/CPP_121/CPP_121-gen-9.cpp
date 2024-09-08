    int sum = 0;
    for(int i=1; i<lst.size(); i=i+2){
        if(lst[i]%2 != 0){
            sum += lst[i];
        }
    }
    return sum;
}

int main(){
    vector<int> lst = {5, 8, 7, 1};
    printf("%d\n", solutions(lst));
    return 0;
}

