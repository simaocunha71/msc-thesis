    vector<int> v;
    for(int i=1;i<=n;i++){
        if(i%2==0){
            int fact=1;
            for(int j=1;j<=i;j++){
                fact*=j;
            }
            v.push_back(fact);
        }
        else{
            int sum=0;
            for(int j=1;j<=i;j++){
                sum+=j;
            }
            v.push_back(sum);
        }
    }
    return v;
}

int main(){
    int n;
    scanf("%d",&n);
    vector<int> ans = f(n);
    for(int i=0;i<n;i++){
        printf("%d ",ans[i]);
    }
    printf("\n");
    return 0;
}

Here, f(n) function is taking integer n as an argument and returns a vector of size n. The vector contains values of factorial of even indices and sum of numbers from 1 to the index for odd indices.

The for loop is used to iterate over each index from 1 to n.

The if-else statement is used to check whether the index is even or odd. If the index is even, it calculates the factorial and pushes it into the vector. If the index is odd, it calculates the sum of numbers from 1 to the index and pushes it into the vector.

The main() function is used to take the input n and call the f(n) function. The returned vector is then printed.

The time complexity of this function is O(n^2) due to the nested for loop.
*/

#include<iostream>
#include<vector>
using namespace std;

vector<int> f(int n){
    vector<int> v;
    for(int i=1;i<=n;i++){
        if(i%2==0){
            int fact=1;
            for(int j=1;j<=i;j++){
                fact*=j;
            }
            v.push_back(