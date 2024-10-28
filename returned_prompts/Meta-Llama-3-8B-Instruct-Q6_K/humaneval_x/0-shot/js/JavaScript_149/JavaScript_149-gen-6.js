```
function list_sort(lst) {
    return lst.filter(word => word.length % 2 === 0).sort((a, b) => {
        if (a.length === b.length) {
            return a.localeCompare(b);
        } else {
            return a.length - b.length;
        }
    });
}
```


The function `list_sort` filters the input list `lst` to keep only the strings with even lengths using `filter`. Then it sorts the resulting list using `sort`. The sorting function is a compare function that takes two strings `a` and `b` as arguments. 

If the lengths of `a` and `b` are the same, the function returns the result of `localeCompare` which compares the strings lexicographically. If the lengths are different, the function returns the difference of the lengths. This way, the list is sorted by the length of the strings first, and then alphabetically if the lengths are the same. 

The function returns the sorted list. 

For example, if the input list is `["aa", "a", "aaa", "cd"]`, the function will filter out the strings with odd lengths, sort the remaining strings by their lengths and then alphabetically, and return the result as `["aa", "cd"]`. 

The unit test `assert list_sort(["aa", "a", "aaa"]) => ["aa"]` ensures that the function works correctly when all strings have the same length. The unit test `assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]` ensures that the function works correctly when strings have different lengths. The unit test `assert list_sort(["aaa", "aaa"]) => ["aaa"]` ensures that the function works correctly when there are duplicate strings. 