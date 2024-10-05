    if (lst.size() <= 1)
        return NULL;

    int first_min = INT_MAX, second_min = INT_MAX;
    for (int i = 0; i < lst.size(); i++) {
        if (lst[i] < first_min) {
            second_min = first_min;
            first_min = lst[i];
        } else if (lst[i] < second_min && lst[i] != first_min) {
            second_min = lst[i];
        }
    }
    if (second_min == INT_MAX)
        return NULL;
    else
        return second_min;
}

int main(){
    vector<int> v1{1, 2, 3, 4, 5};
    vector<int> v2{5, 1, 4, 3, 2};
    vector<int> v3{};
    vector<int> v4{1, 1};
    printf("%d\n", next_smallest(v1));
    printf("%d\n", next_smallest(v2));
    printf("%d\n", next_smallest(v3));
    printf("%d\n", next_smallest(v4));
    return 0;
}

*/

//Q4/main.cpp
/*
