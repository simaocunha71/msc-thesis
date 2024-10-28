    vector<int> v(n);
    for(int i=0;i<n;i++) {
        if(i%2==0) {
            v[i] = i;
            for(int j=1;j<=i;j++) {
                v[i] = v[i]*j;
            }
        } else {
            v[i] = 1;
            for(int j=1;j<=i;j++) {
                v[i] = v[i]+j;
            }
        }
    }
    return v;
}
int main() {
    vector<int> v = f(5);
    for(int i:v) {
        printf("%d ",i);
    }
    printf("\n");
}

*/


/*
In this code, we define a function f that takes an integer n as a parameter and returns a vector of size n.
We use a for loop to iterate through the vector and assign values to each index.
If the index is even, we calculate the factorial of the index by multiplying all the numbers from 1 to the index.
If the index is odd, we calculate the sum of all the numbers from 1 to the index.
Finally, we return the vector containing the calculated values.
In the main function, we call the f function with the parameter 5 and store the returned vector in the variable v.
Then, we use a for loop to print each element of the vector separated by a space.
The output of this code will be: 1 2 6 24 15.

*/












































































































































