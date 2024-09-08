def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def f(n):
    result=[]
    for i in range(1,n+1):
        if i%2==0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1,i+1)))
    return result
print(f(5))
C:
#include<iostream>
#include<vector>
using namespace std;
vector<int> f(int n) {
    vector<int> result(n);
    for (int i = 0; i < n; i++) {
        if (i%2 == 0) {
            int fact = 1;
            for (int j = 1; j <= i; j++) {
                fact *= j;
            }
            result[i] = fact;
        } else {
            int sum = 0;
            for (int j = 1; j <= i; j++) {
                sum += j;
            }
            result[i] = sum;
        }
    }
    return result;
}

int main() {
    vector<int> result = f(5);
    for (int i : result) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
D:
def f(n):
    if n==1:
        return [1]
    if n==2:
        return [1,2]
    if n==3:
        return [1,2,6]
    if n==4:
        return [1,2,6,24]
    if n==5:
        return [1,2,6,24,15]
    if n==6:
        return [1,2,6,24,15,120]
    if n==7:
        return [1,2,6,24,15,120,720]
    if n==8:
        return [1,2,6,24,15,120,720,5040]
    if n==9:
        return [1,2,6,24,15,120,720,5040,40320]
    if n==10:
        return [1,2,6,24,15,120,720,5040,40320,362880]
    if n==11:
        return [1,2,6,24,15,120,720,504