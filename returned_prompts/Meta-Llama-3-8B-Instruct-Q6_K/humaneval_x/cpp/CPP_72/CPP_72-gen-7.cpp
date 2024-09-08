    // Check if q is balanced
    bool is_balanced = true;
    for(int i = 0; i < q.size() / 2; i++){
        if(q[i] != q[q.size() - i - 1]){
            is_balanced = false;
            break;
        }
    }
    
    // Check if the sum of q is less than or equal to w
    int sum = 0;
    for(int i = 0; i < q.size(); i++){
        sum += q[i];
    }
    bool is_light = sum <= w;
    
    // Return true if q is balanced and the sum of q is less than or equal to w
    return is_balanced && is_light;
}

int main() {
    vector<int> q1 = {1, 2};
    vector<int> q2 = {3, 2, 3};
    vector<int> q3 = {3, 2, 3};
    vector<int> q4 = {3};
    printf("%d\n", will_it_fly(q1, 5)); // false
    printf("%d\n", will_it_fly(q2, 1)); // false
    printf("%d\n", will_it_fly(q3, 9)); // true
    printf("%d\n", will_it_fly(q4, 5)); // true
    return 0;
}

B:
    // Check if q is balanced
    bool is_balanced = true;
    for(int i = 0; i < q.size() / 2; i++){
        if(q[i] != q[q.size() - i - 1]){
            is_balanced = false;
            break;
        }
    }
    
    // Check if the sum of q is less than or equal to w
    int sum = 0;
    for(int i = 0; i < q.size(); i++){
        sum += q[i];
    }
    bool is_light = sum <= w;
    
    // Return true if q is balanced and the sum of q is less than or equal to w
    return is_balanced && is_light;
}

int main() {
    vector<int> q1 = {1, 2};
    vector<int> q2 = {3, 2, 3};
    vector<int> q3 = {3, 2, 3};
    vector<int> q4 = {3};
    printf("%d