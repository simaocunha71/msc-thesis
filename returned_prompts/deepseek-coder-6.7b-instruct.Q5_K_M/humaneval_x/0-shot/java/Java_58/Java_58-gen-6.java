        // sort both lists
        Collections.sort(l1);
        Collections.sort(l2);

        // create a new list to store the common elements
        List<Integer> commonList = new ArrayList<>();

        // use two pointers to traverse the lists
        int i = 0, j = 0;
        while (i < l1.size() && j < l2.size()) {
            if (l1.get(i) < l2.get(j)) {
                i++;
            } else if (l1.get(i) > l2.get(j)) {
                j++;
            } else {
                // find common element
                commonList.add(l1.get(i));
                i++;
                j++;
            }
        }

        return commonList;
    }
}

Here, we are using the two-pointer technique to solve this problem. The common part is that the two lists are sorted. The time complexity is O(nlogn + mlogm + n + m), where n and m are the sizes of l1 and l2, respectively. The space complexity is O(n + m), where n and m are the sizes of l1 and l2, respectively.


A: Here is the python solution:

```python
def common(l1, l2):
    return sorted(set(l1).intersection(set(l2)))

print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # outputs [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # outputs [2, 3]
```

In this solution, we use the built-in set data structure to find the intersection of the two lists. The intersection operation returns a new set with elements common to both sets. The intersection operation has O(min(len(s1), len(s2))) time complexity, where len(s1) and len(s2) are the lengths of the two input sets