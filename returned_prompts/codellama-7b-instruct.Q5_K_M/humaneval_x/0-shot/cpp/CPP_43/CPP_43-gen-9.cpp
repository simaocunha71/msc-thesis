    for(int i=0; i<l.size(); i++){
        for(int j=i; j<l.size(); j++){
            if(l[i]+l[j]==0){
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
    bool r1, r2, r3, r4, r5;
    r1 = pairs_sum_to_zero(l1);
    r2 = pairs_sum_to_zero(l2);
    r3 = pairs_sum_to_zero(l3);
    r4 = pairs_sum_to_zero(l4);
    r5 = pairs_sum_to_zero(l5);
    printf("pairs_sum_to_zero({1, 3, 5, 0}) == %s\n", r1? "true" : "false");
    printf("pairs_sum_to_zero({1, 3, -2, 1}) == %s\n", r2? "true" : "false");
    printf("pairs_sum_to_zero({1, 2, 3, 7}) == %s\n", r3? "true" : "false");
    printf("pairs_sum_to_zero({2, 4, -5, 3, 5, 7}) == %s\n", r4? "true" : "false");
    printf("pairs_sum_to_zero({1}) == %s\n", r5? "true" : "false");
}
