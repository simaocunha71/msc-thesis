/*
Implement the function f that takes n as a parameter,
and returns a vector of size n, such that the value of the element at index i is the factorial of i if i is even
or the sum of numbers from 1 to i otherwise.
i starts from 1.
the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
Example:
f(5) == {1, 2, 6, 24, 15}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> f(int n){
    vector<int> ans;
    int i = 0, j, x, y;
    while(i < n)
    {
        if((i+1)%2 == 0 && i != 1 )
            ans.push_back(j);
        else
            for (int k=x=1;k<=(n-i+1);k++){
                j = x*y;
                y++;}
            ans.push_back(j);
        i += 2;
    }
    return ans;
}

//This is the implementation of f which takes n as an input parameter and returns a vector of size n, such that the value of the element at index i is the factorial of i if i is even or the sum of numbers from 1 to i otherwise
int main(void) {
    int n;
    scanf("%d",&n);

    vector<int> ans = f(n);
    for (int i = 0; i < n; i++)
        printf("%d, ",ans[i]);
  
    return 0;
}
