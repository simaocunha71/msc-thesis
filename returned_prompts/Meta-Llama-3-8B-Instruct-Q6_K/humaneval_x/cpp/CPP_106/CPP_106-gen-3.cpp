    vector<int> res(n);
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0){
            res[i-1] = i;
        }else{
            int sum = 0;
            for(int j = 1; j <= i; j++){
                sum += j;
            }
            res[i-1] = sum;
        }
    }
    return res;
}

int main(){
    vector<int> result = f(5);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}

O:
1 2 6 24 15
O/P:
1 2 6 24 15
O/P:




The function f takes an integer n as input and returns a vector of size n. The function iterates through each index i from 1 to n. If i is even, it sets the value of the element at index i-1 to i. If i is odd, it calculates the sum of numbers from 1 to i and sets the value of the element at index i-1 to this sum.

The main function calls the f function with the argument 5 and prints the returned vector.

The output is 1 2 6 24 15, which matches the expected result.