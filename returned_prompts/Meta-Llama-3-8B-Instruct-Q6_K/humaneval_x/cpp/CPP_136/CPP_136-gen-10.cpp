    int a = -2147483648; // the maximum negative integer
    int b = 2147483647; // the maximum positive integer
    for(int i = 0; i < lst.size(); i++){
        if(lst[i] < 0 && lst[i] > a){
            a = lst[i];
        }
        else if(lst[i] > 0 && lst[i] < b){
            b = lst[i];
        }
    }
    vector<int> result;
    result.push_back(a);
    result.push_back(b);
    if(a == -2147483648 || b == 2147483647){
        result = {0,0};
    }
    return result;
}

int main() {
    vector<int> lst = {2, 4, 1, 3, 5, 7};
    vector<int> result = largest_smallest_integers(lst);
    printf("(%d, %d)\n", result[0], result[1]);
    return 0;
}
