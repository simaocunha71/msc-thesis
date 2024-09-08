    int sum = 0;
    for(int i = 1; i < lst.size(); i += 2){
        if(i < lst.size()) sum += lst[i];
    }
    return sum;
}

int main() {
    vector<int> lst = {4, 2, 6, 7};
    printf("%d\n", add(lst));
    return 0;
} 
