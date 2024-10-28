    sort(arr.begin(),arr.end());
    vector<int> result;
    int len = arr.size();
B:
    for(int i=len-1;i>=len-k;i--){
        result.push_back(arr[i]);
    }
    return result;
}

int main(){
    vector<int> arr = {-3, -4, 5};
    int k = 3;
    vector<int> result = maximum(arr, k);
    for(int i=0;i<result.size();i++){
        printf("%d ",result[i]);
    }
    return 0;
}
```

# 3. C++ Solution

```cpp
#include<iostream>
#include<vector>
#include<queue>
using namespace std;

vector<int> maximum(vector<int> arr,int k){
    priority_queue<int> pq(arr.begin(),arr.end());
    vector<int> result;
    for(int i = 0; i < k; i++){
        result.push_back(pq.top());
        pq.pop();
    }
    return result;
}

int main(){
    vector<int> arr = {-3, -4, 5};
    int k = 3;
    vector<int> result = maximum(arr, k);
    for(int i=0;i<result.size();i++){
        cout<<result[i]<<" ";
    }
    return 0;
}
```

# 4. Java Solution

```java
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static ArrayList<Integer> maximum(int[] arr, int k) {
        Queue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        ArrayList<Integer> result = new ArrayList<>();
        for(int i: arr) {
            queue.add(i);
        }
        for(int i = 0; i < k; i++