
const filterEvenSort = (lst) => {
  const evenLengthWords = lst.filter(word => word.length % 2 === 0);
  return evenLengthWords.sort((a, b) => a.length - b.length || a.localeCompare(b));
};

console.log(filterEvenSort(["aa", "a", "aaa"]));  //=> ["aa"]
console.log(filterEvenSort(["ab", "a", "aaa", "cd"]));  //=> ["ab", "cd"]

// Here, the function filterEvenSort filters out the words with odd lengths,
// then sorts them according to their length, and then alphabetically.

```



```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


