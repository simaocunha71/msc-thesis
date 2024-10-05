    vector<int> res;
    for(int i=0;i<x.size();i++){
        int num=x[i];
        bool flag=false;
        while(num>0){
            int digit=num%10;
            if(digit%2==0){
                flag=true;
                break;
            }
            num/=10;
        }
        if(!flag){
            res.push_back(x[i]);
        }
    }
    sort(res.begin(),res.end());
    return res;
}
int main(){
    vector<int> v={15,33,1422,1};
    vector<int> result=unique_digits(v);
    for(int i=0;i<result.size();i++){
        printf("%d ",result[i]);
    }
    return 0;
}
```




```python
# Python solution

def unique_digits(x):
    res = []
    for num in x:
        if all(int(digit) % 2 != 0 for digit in str(num)):
            res.append(num)
    return sorted(res)

# test case
print(unique_digits([15, 33, 1422, 1]))  # [1, 15, 33]
print(unique_digits([152, 323, 1422, 10]))  # []
```




```java
// Java solution
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static List<Integer> uniqueDigits(List<Integer> x) {
        List<Integer> res = new ArrayList<>();
        for (int num : x) {
            if (String.valueOf(num).chars().allMatch(c -> (c - '0') % 2 != 0)) {
                res.add(num);
            }
        }
        Collections.sort(res);
        return res;
    }