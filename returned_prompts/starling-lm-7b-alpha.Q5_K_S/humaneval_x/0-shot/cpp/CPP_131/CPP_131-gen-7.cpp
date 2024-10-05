O(logn)解法：
首先，我们需要对整数进行拆分，将整数拆分成各个位的积，然后我们可以从每一位上开始进行判断，如果该位是奇数，我们就将其乘以后面所有的积，如果是偶数，我们就跳过，直到整个数字被遍历完成。

以下为C++代码：

```
#include<iostream>
using namespace std;

int digits(int n){
    if(n==0)
        return 0;
    else if(n%2!=0)
        return n*digits(n/10);
    else
        return digits(n/10);
}

int main(){
    int n;
    cin>>n;
    cout<<digits(n);
    return 0;
}
```

以下为Python代码：

```
def digits(n):
    if n == 0:
        return 0
    elif n % 2 != 0:
        return n * digits(n // 10)
    else:
        return digits(n // 10)

n = int(input())
print(digits(n))
```

以下为Java代码：

```
public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        System.out.println(digits(n));
    }

    public static int digits(int n) {
        if (n == 0) {
            return