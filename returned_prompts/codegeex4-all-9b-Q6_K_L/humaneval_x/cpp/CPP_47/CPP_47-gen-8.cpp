/*
Return median of elements in the vector l.
>>> median({3, 1, 2, 4, 5})
3
>>> median({-10, 4, 6, 1000, 10, 20})
15.0
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){

    //Write your code here
    sort(l.begin(),l.end());
    int n=l.size();
    float median;
    if(n%2==0)
    {
        median=(float)(l[n/2-1]+l[n/2])/2;
    }
    else
    {
        median=(float)(l[n/2]);
    }
    return median;
}
int main() {
   vector<float> l = {3, 1, 2, 4, 5};
   // l.push_back(3);
   // l.push_back(1);
   // l.push_back(2);
   // l.push_back(4);
   // l.push_back(5);
   printf("%.6f\n",median(l));
   l = {3, 1, 2, 4, 5};
   printf("%.6f\n",median(l));
   l = {-10, 4, 6, 1000, 10, 20};
   printf("%.6f\n",median(l));
   return 0;
}
请问代码有什么问题？

你的代码逻辑是正确的，它正确地计算了输入向量的中位数。然而，它有一个小问题：当向量长度为奇数时，你返回的是整数而不是浮点数。这是因为你在计算中位数时，直接使用了整数除法（`n/2`），这会导致结果总是整数。

在你的代码中，当`n`为奇数时，`n/2`的值是一个整数，因此`l[n/2]`的结果也是一个整数。为了确保无论`n`是奇数还是偶数，返回的中位数都是浮点数，你需要在计算中位数时使用浮点数除法（`n/2.0`）。

以下是修改后的代码：

```cpp
float median(vector<float> l){
    sort(l.begin(),l.end());
    int n=l.size();
    float median;
    if(n%2==0)
    {
        median=(float)(l[n/2-1]+l[n/2])/