    int n = lst.size();
    int freq[n+1] = {0};
    for(int i=0; i<n; i++)
        freq[lst[i]]++;
    for(int i=n; i>0; i--)
        if(freq[i] >= i)
            return i;
    return -1;
}

int main() {
    vector<int> v1 = {4, 1, 2, 2, 3, 1};
    vector<int> v2 = {1, 2, 2, 3, 3, 3, 4, 4, 4};
    vector<int> v3 = {5, 5, 4, 4, 4};
    printf("%d\n", search(v1));
    printf("%d\n", search(v2));
    printf("%d\n", search(v3));
    return 0;
}
*/

S:
The solution starts by creating an array `freq` of size `n+1` and all elements initially set to 0. 
Then for each element `i` in the input vector, we increment the `freq[i]`.
After that, we start from the largest possible integer (`n`) and check if the frequency of `i` is greater than or equal to `i`. 
If so, we return `i`. If no such integer is found, we return `-1`.

The time complexity of this solution is O(n) and the space complexity is O(n) as we create a frequency array of size `n+1`.
*/


























































































































