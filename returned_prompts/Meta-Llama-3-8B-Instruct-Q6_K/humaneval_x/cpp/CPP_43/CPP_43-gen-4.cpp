    vector<int> :: iterator it;
    for(it = l.begin(); it != l.end(); ++it){
        for(int j = it + 1; j < l.end(); ++j){
            if(*it + *j == 0){
                return true;
            }
        }
    }
    return false;
}
int main(){
    vector<int> l;
    l.push_back(1);
    l.push_back(2);
    l.push_back(3);
    l.push_back(7);
    printf("%d\n", pairs_sum_to_zero(l));
    return 0;
}

S:
The function `pairs_sum_to_zero` takes a vector of integers as input and returns `true` if there are two distinct elements in the vector that sum to zero, and `false` otherwise.

The function uses two nested loops to iterate over all pairs of distinct elements in the vector. For each pair, it checks if their sum is zero. If it finds such a pair, it returns `true`. If it doesn't find any such pair after checking all pairs, it returns `false`.

In the `main` function, we create a vector `l` and add the elements 1, 2, 3, and 7 to it. We then call `pairs_sum_to_zero` with `l` as the argument and print the result.

The output of this program is `false`, which means that there are no two distinct elements in the vector that sum to zero.

This solution has a time complexity of O(n^2), where n is the number of elements in the input vector. This is because it uses two nested loops to iterate over all pairs of distinct elements. The space complexity is O(1), as it only uses a constant amount of space to store the input vector and the result. 





