    vector<int> a(n);
    for(int i = 1; i <= n; i++){
        a[i - 1] = i * i - i + 1;
    }
    int count = 0;
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            for(int k = j + 1; k < n; k++){
                if((a[i] + a[j] + a[k]) % 3 == 0){
                    count++;
                }
            }
        }
    }
    return count;
}

int main()
{
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    printf("The number of triples is %d\n", get_matrix_triples(n));
    return 0;
}
//  Time complexity : O(n^3)
//  Space complexity : O(n) for the input array
//  This solution uses three nested loops to generate all possible triples and checks if their sum is divisible by 3.
//  It can be optimized by using a hash map to store the sum of each triple and check if it is already present in the map. This would reduce the time complexity to O(n^2). 
//  However, this would increase the space complexity to O(n). 
//  The time complexity can also be reduced to O(n log n) by sorting the array first and then using two pointers to generate the triples. This would also increase the space complexity to O(n). 
//  The choice of the solution depends on the constraints of the problem and the available resources. 
//  In this case, the problem statement does not specify any constraints, so any of the above solutions can be used. 

//  To further optimize the code, we can use the following trick: 
//  We can calculate the sum of the triple modulo 3 first, and then check if it is 0. 
//  If it is 0, then we know that the sum is divisible by 3, so we can increment the count. 
//  This would reduce the time complexity to O(n^2) because we would only need to check if the sum is 0, and not calculate the actual sum. 
//  The space complexity would remain the same, O(n). 

//  Here is the optimized code: 
int get_matrix_triples(int n){
    vector<int> a(n