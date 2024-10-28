  let filteredList = lst.filter(word => word.length % 2 === 0);
  return filteredList.sort((a, b) => a.length - b.length || a.localeCompare(b));
}
```


