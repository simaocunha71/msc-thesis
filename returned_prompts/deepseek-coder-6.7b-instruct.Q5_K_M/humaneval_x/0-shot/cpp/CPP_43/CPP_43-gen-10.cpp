    int len = l.size();
    for(int i=0; i<len; i++){
        for(int j=i+1; j<len; j++){
            if(l[i] + l[j] == 0){
                return true;
            }
        }
    }
    return false;
}

int main(){
    vector<int> l1 = {1, 3, 5, 0};
    vector<int> l2 = {1, 3, -2, 1};
    vector<int> l3 = {1, 2, 3, 7};
    vector<int> l4 = {2, 4, -5, 3, 5, 7};
    vector<int> l5 = {1};

    printf("%d\n", pairs_sum_to_zero(l1));
    printf("%d\n", pairs_sum_to_zero(l2));
    printf("%d\n", pairs_sum_to_zero(l3));
    printf("%d\n", pairs_sum_to_zero(l4));
    printf("%d\n", pairs_sum_to_zero(l5));

    return 0;
}

