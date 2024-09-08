    // check if it's balanced
    bool is_balanced = true;
    for(int i = 0; i < q.size(); i++){
        if(q[i] != q[q.size() - i - 1]){
            is_balanced = false;
            break;
        }
    }
    if(!is_balanced){
        return false;
    }

    // check if the sum of its elements is less than or equal the maximum possible weight
    int sum = 0;
    for(int i = 0; i < q.size(); i++){
        sum += q[i];
    }
    if(sum > w){
        return false;
    }
    return true;
}
int main(){
    printf("%d\n", will_it_fly({3,2,3},9));
    return 0;
}
Output:
1
*/



