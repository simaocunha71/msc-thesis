    int sum=0;
    for(int i=1; i<lst.size(); i+=2){
        if(lst[i]%2==0)
            sum+=lst[i];
    }
    return sum;
}
int main()
{
    vector<int> lst={4, 2, 6, 7};
    printf("%d\n", add(lst));
    return 0;
}
A solution is:

```c
#include<stdio.h>
#include<vector>
using namespace std;
int add(vector<int> lst){
    int sum=0;
    for(int i=1; i<lst.size(); i+=2){
        if(lst[i]%2==0)
            sum+=lst[i];
    }
    return sum;
}
int main()
{
    vector<int> lst={4, 2, 6, 7};
    printf("%d\n", add(lst));
    return 0;
}
```

This solution iterates over the vector, starting from the second element (index 1) to the last element. If the current element is even, it adds it to the sum. Finally, it returns the sum. The time complexity of this solution is O(n), where n is the size of the vector. The space complexity is O(1), as it only uses a constant amount of space.