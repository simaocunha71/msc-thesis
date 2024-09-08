    int max_neg = INT_MIN;
    int min_pos = INT_MAX;
    bool neg_found = false;
    bool pos_found = false;

    for(int i = 0; i < lst.size(); i++){
        if(lst[i] < 0){
            if(lst[i] > max_neg){
                max_neg = lst[i];
                neg_found = true;
            }
        }else if(lst[i] > 0){
            if(lst[i] < min_pos){
                min_pos = lst[i];
                pos_found = true;
            }
        }
    }
    if(neg_found && pos_found){
        return {max_neg, min_pos};
    }
    return {0,0};

}
int main(){
    vector<int> lst1 = {2, 4, 1, 3, 5, 7};
    vector<int> lst2 = {};
    vector<int> lst3 = {0};
    vector<int> lst4 = {1, 2, 3};
    vector<int> result1 = largest_smallest_integers(lst1);
    vector<int> result2 = largest_smallest_integers(lst2);
    vector<int> result3 = largest_smallest_integers(lst3);
    vector<int> result4 = largest_smallest_integers(lst4);

    printf("largest_smallest_integers({2, 4, 1, 3, 5, 7}) == {%d, %d}\n", result1[0], result1[1]);
    printf("largest_smallest_integers({}) == {%d, %d}\n", result2[0], result2[1]);
    printf("largest_smallest_integers({0}) == {%d, %d}\n", result3[0], result3[1]);
    printf("largest_smallest_integers({1, 2, 3}) == {%d, %d}\n", result4[0], result4[1]);
    return 0;
}

