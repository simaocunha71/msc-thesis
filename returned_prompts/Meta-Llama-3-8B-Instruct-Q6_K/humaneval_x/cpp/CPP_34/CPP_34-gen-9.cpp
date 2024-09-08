    vector<int> v;
    for(auto x : l){
        if(find(v.begin(), v.end(), x) == v.end()) v.push_back(x);
    }
    sort(v.begin(), v.end());
    return v;
}

int main(){
    vector<int> l = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> result = unique(l);
    for(auto x : result) printf("%d ", x);
    printf("\n");
    return 0;
}

Output:
0 2 3 5 9 123
*/



Explanation:
The problem asks to create a function `unique` that takes a vector of integers as input and returns a new vector containing the unique elements in the same order they first appear in the input vector, sorted in ascending order.

The function `unique` is implemented using a simple algorithm:

1. Create an empty vector `v` to store the unique elements.
2. Iterate through the input vector `l`. For each element `x`, check if it exists in the `v` using the `find` function. If it does not exist, add it to `v`.
3. Sort the `v` vector in ascending order using the `sort` function.
4. Return the `v` vector.

In the `main` function, we create a sample vector `l` and call the `unique` function to get the unique and sorted elements. We then print the result using a loop.

The output is a sorted and unique vector of integers: `0 2 3 5 9 123`.