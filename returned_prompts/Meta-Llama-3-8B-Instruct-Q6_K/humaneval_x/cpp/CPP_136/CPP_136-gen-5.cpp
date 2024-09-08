    int a = -1, b = 1;
    for(int i = 0; i < lst.size(); i++){
        if(lst[i] > 0 && lst[i] < b){
            b = lst[i];
        }
        if(lst[i] < 0 && lst[i] > a){
            a = lst[i];
        }
    }
    vector<int> result;
    result.push_back(a);
    result.push_back(b);
    return result;
}

int main() {
    vector<int> lst = {2, 4, 1, 3, 5, 7};
    vector<int> result = largest_smallest_integers(lst);
    printf("Result: ");
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}
