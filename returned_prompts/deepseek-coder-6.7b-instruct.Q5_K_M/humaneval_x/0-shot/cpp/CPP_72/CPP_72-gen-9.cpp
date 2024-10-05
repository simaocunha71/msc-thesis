    int sum = 0;
    for(int i=0; i<q.size(); i++){
        sum += q[i];
    }
    if(sum > w){
        return false;
    }
    for(int i=0; i<q.size()/2; i++){
        if(q[i] != q[q.size()-i-1]){
            return false;
        }
    }
    return true;
}

int main() {
    printf("%d\n",will_it_fly({1,2}, 5);
    printf("%d\n",will_it_fly({3,2,3}, 1);
    printf("%d\n",will_it_fly({3,2,3}, 9);
    printf("%d\n",will_it_fly({3}, 5);
    return 0;
}

*/

// Code:
bool will_it_fly(vector<int> q, int w){
    int sum = 0;
    for(int i=0; i<q.size(); i++){
        sum += q[i];
    }
    if(sum > w){
        return false;
    }
    for(int i=0; i<q.size()/2; i++){
        if(q[i] != q[q.size()-i-1]){
            return false;
        }
    }
    return true;
}

int main() {
    printf("%d\n",will_it_fly({1,2}, 5));
    printf("%d\n",will_it_fly({3,2,3}, 1));
    printf("%d\n",will_it_fly({3,2,3}, 9));
    printf("%d\n",will_it_fly({3}, 5));
    return 0;
}

// Explanation:
// The function `will_it_fly` takes a vector `q` and an integer `w` as input. 
// It first calculates the sum of the elements in `q` and checks if this sum is greater than `w`. 
//