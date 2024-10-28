        Collections.sort(l);
        for(int i=0; i<l.size()-2; i++){
            int j = i+1;
            int k = l.size()-1;
            while(j<k){
                if(l.get(i)+l.get(j)+l.get(k) == 0){
                    return true;
                }
                else if(l.get(i)+l.get(j)+l.get(k) < 0){
                    j++;
                }
                else{
                    k--;
                }
            }
        }
        return false;
    }
}


A: This is a good question and the problem can be solved by using a two-pointer technique.

Here is an efficient Python solution which uses two pointers to find a triplet that sums to zero.

```python
def triplesSumToZero(l):
    l.sort()
    for i in range(len(l)-2):
        if i>0 and l[i]==l[i-1]:
            continue
        j, k = i+1, len(l)-1
        while j<k:
            sum = l[i]+l[j]+l[k]
            if sum<0:
                j += 1
            elif sum>0:
                k -= 1
            else:
                return True
    return False
```

This solution works by first sorting the input list and then for each number, it uses a two-pointer approach to find two other numbers that sum to -current number. If it finds such two numbers, it returns True. If it doesn't find any such triplet, it returns False.

The time complexity of this solution is O(n^2), where n is the length of the list.

It's worth mentioning that this solution assumes that the input list doesn't contain any duplicate numbers. If the input list can contain duplicate numbers, you should add a check to skip duplicate numbers while finding the triplets.

Also, this solution assumes that the input list can contain negative numbers. If the input list can only contain positive numbers, you should add a check to return False if the current number is positive.