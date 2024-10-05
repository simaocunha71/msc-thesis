    for(int i=0; i<lst.size()-1; i++){
        if(lst[i] >= lst[i+1])
            return false;
    }
    return true;
}

int main(){
    printf("%d\n", is_sorted({5}));
    printf("%d\n", is_sorted({1, 2, 3, 4, 5}));
    printf("%d\n", is_sorted({1, 3, 2, 4, 5}));
    printf("%d\n", is_sorted({1, 2, 3, 4, 5, 6}));
    printf("%d\n", is_sorted({1, 2, 3, 4, 5, 6, 7}));
    printf("%d\n", is_sorted({1, 2, 2, 3, 3, 4}));
    printf("%d\n", is_sorted({1,