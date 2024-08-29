    for(int i=0;i<arr.size();i++){
        for(int j=0;j<arr.size()-i-1;j++){
            int a=0,b=0;
            int temp=arr[j];
            while(temp){
                a+=temp%2;
                temp/=2;
            }
            temp=arr[j+1];
            while(temp){
                b+=temp%2;
                temp/=2;
            }
            if(a>b){
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }

    return arr;
}
int main(){
    vector<int> v={1, 5, 2, 3, 4};
    vector<int> v1=sort_array(v);
    for(auto i:v1){
        printf("%d ",i);
    }
    printf("\n");
    return 0;
}
请问如何优化这段代码

这段代码的基本思路是正确的，但是它的效率可以进一步优化。当前的实现方式是使用了冒泡排序，其时间复杂度是O(n^2)，当数据量较大时，效率会比较低。

一种优化的方式是使用计数排序，利用每个数字的二进制表示中1的个数进行排序。这种方法的时间复杂度可以降低到O(n)，其中n是数组中的元素个数。

以下是使用计数排序优化后的代码：

```cpp
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

vector<int> sort_array(vector<int> arr) {
    // 计算数组中最大的数字
    int max_val = *max_element(arr.begin(), arr.end());
    
    // 创建一个计数数组，用于记录每个数字的二进制表示中1的个数
    vector<int> count(32, 0);
    for (int num : arr) {
        int index = 0;
        while (num > 0) {
            count[index++] += num & 1;
            num >>= 1;
        }
    }

    // 创建一个结果数组，用于存储排序后的结果
    vector<int> result(arr.size());
    int index = 0;
    for (int i = 0; i < 32; ++i) {
        for (int j = 0; j < count[i]; ++j) {
            result[index++] = pow(2, i);
        }
    }

    return result;
}

int main() {
    vector<int> v = {1, 5,