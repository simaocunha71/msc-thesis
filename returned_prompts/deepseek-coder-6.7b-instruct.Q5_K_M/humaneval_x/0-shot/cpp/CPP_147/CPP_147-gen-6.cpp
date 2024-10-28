    /*
    vector<int> a(n);
    for(int i = 1; i <= n; i++){
        a[i-1] = i*i - i + 1;
    }
    int count = 0;
    for(int i = 0; i < n-2; i++){
        for(int j = i+1; j < n-1; j++){
            for(int k = j+1; k < n; k++){
                if((a[i] + a[j] + a[k]) % 3 == 0){
                    count++;
                }
            }
        }
    }
    return count;
    */
    int count = 0;
    for(int i = 1; i <= n; i++){
        for(int j = i+1; j <= n; j++){
            for(int k = j+1; k <= n; k++){
                if(((i*i - i + 1) + (j*j - j + 1) + (k*k - k + 1)) % 3 == 0){
                    count++;
                }
            }
        }
    }
    return count;
}

int main(){
    int n = 5;
    printf("%d\n", get_matrix_triples(n));
    return 0;
}

//This question requires understanding of combinatorial mathematics and modulo arithmetic. 
//The solution provided works by iterating through all possible triplets of the given array and checking if the sum of their values is a multiple of 3. 
//This is done by using the modulo operator '%', which gives the remainder of the division. 
//If the remainder of the division is 0, then the sum is a multiple of 3.
//The time complexity of this solution is O(n^3), which is quite high for large n.
//This solution works perfectly, but it's not efficient and can be improved by using combinatorial mathematics and modulo arithmetic.
//This solution is also not correct, as it doesn't consider the condition that i < j < k.
//The correct solution should be:
//count += ((i*j*k)%3 == 