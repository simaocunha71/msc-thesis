        ArrayList<Integer> sortedEvenIdxNums = new ArrayList<>();
        ArrayList<Integer> result = new ArrayList<>();

        for(int i = 0; i < l.size(); i++) {
            if(i % 2 == 0) {
                sortedEvenIdxNums.add(l.get(i));
            }
        }

        Collections.sort(sortedEvenIdxNums);

        int sortedEvenIdxNumsIndex = 0;

        for(int i = 0; i < l.size(); i++) {
            if(i % 2 == 0) {
                result.add(sortedEvenIdxNums.get(sortedEvenIdxNumsIndex++));
            } else {
                result.add(l.get(i));
            }
        }

        return result;
    }
}


A: Here's a solution which does not use additional space and has a time complexity of O(n log n):

```
class Solution {
    /**
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sortEven(Arrays.asList(1, 2, 3))
     [1, 2, 3]
    >>> sortEven(Arrays.asList(5, 6, 3, 4))
     [3, 6, 5, 4]
     */
    public List<Integer> sortEven(List<Integer> l) {
        List<Integer> evens = new ArrayList<>();
        for (int i = 0; i < l.size(); i += 2) {
            evens.add(l.get(i));
        }
        Collections.sort(evens);
        for (int i = 0, j = 0; i < l.size(); i += 2, ++j) {
            l.set(i, evens.get(j));
        }
        return l;
    }
}
```

In this solution, we first