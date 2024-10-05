        List<Integer> result = new ArrayList<Integer>();
        if (lst.size() == 0)
            return result;
        Collections.sort(lst);
        int start = 0;
        int end = lst.size() - 1;
        boolean flag = true;
        while (start <= end) {
            if (flag) {
                result.add(lst.get(start));
                start++;
            } else {
                result.add(lst.get(end));
                end--;
            }
            flag = !flag;
        }
        return result;
    }
}

In the above solution, we sort the given list first, then we start picking elements from the start and end alternately and add them to the result list. We flip the boolean flag after each addition to decide whether to pick the next minimum or maximum. If flag is true, we pick the next minimum, else we pick the next maximum.

This solution has a time complexity of O(n log n) due to the sorting of the list, where n is the size of the list. The space complexity is O(n) for the result list.

I hope this solution is helpful. If you have any further questions, please feel free to ask.


A: Here is a solution in Python:

```python
def strange_sort_list(lst):
    lst.sort()
    result = []
    while lst:
        result.append(lst.pop(0))
        if lst:
            result.append(lst.pop())
    return result
```
This solution sorts the list in ascending order, then pops the smallest and largest remaining elements from the list and appends them to the result list. The process is repeated until the list is empty.

The time complexity of this solution is O(n log n) due to the sorting operation, where n is the size of the list. The space complexity is O(n) for the result list.

If you have any further questions, please feel free to ask.

```

A: 
    List<Integer> result = new ArrayList<Integer>();
    if (lst.size() == 0)
        return result;
    Collections