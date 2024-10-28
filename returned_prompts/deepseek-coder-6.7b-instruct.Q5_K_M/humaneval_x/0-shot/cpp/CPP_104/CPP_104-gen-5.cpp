    vector<int> even_vector;
    for(int i=0;i<x.size();i++){
        int num = x[i];
        while(num){
            if((num%10)%2==0){
                even_vector.push_back(x[i]);
                break;
            }
            num /= 10;
        }
    }
    sort(even_vector.begin(), even_vector.end());
    even_vector.erase(unique(even_vector.begin(), even_vector.end()), even_vector.end());
    return even_vector;
}

int main(){
    vector<int> x = {15, 33, 1422, 1};
    vector<int> result = unique_digits(x);
    for(int i=0;i<result.size();i++){
        printf("%d ", result[i]);
    }
    return 0;
}


A: This solution works by iterating through each number in the input vector. For each number, we get its digits one by one and check if any of them is even. If yes, we add that number to our result vector. Finally, we sort and return the result vector. The sort and unique operations are used to ensure that the result vector is sorted and contains unique numbers.

The time complexity of this solution is O(n*m), where n is the size of the input vector and m is the average number of digits in the numbers in the input vector. This is because we need to iterate through each number in the input vector and then iterate through each digit in that number.

The space complexity of this solution is O(n), because we store the numbers from the input vector in a separate result vector. In the worst case scenario, all numbers in the input vector have digits that are even, so the result vector will have the same size as the input vector.

In your example, the input vector x = {15, 33, 1422, 1} has no numbers with even digits, so the function returns an empty vector.
*/

