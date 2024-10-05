        List<String> result = new ArrayList<String>();
        for(String str : lst) {
            if(str.length() % 2 == 0) {
                result.add(str);
            }
        }
        Collections.sort(result, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                if(s1.length() == s2.length()) {
                    return s1.compareTo(s2);
                }
                return s1.length() - s2.length();
            }
        });
        return result;
    }
}


A: Here is a more simple and compact way to do it by using Java 8 streams.

```
public List<String> listSort(List<String> lst) {
    return lst.stream()
            .filter(s -> s.length() % 2 == 0)
            .sorted(Comparator.comparing(String::length).thenComparing(String::compareTo))
            .collect(Collectors.toList());
}
```

In the stream, we filter out the strings that have odd lengths, then we sort them by length and alphabetically using `Comparator.comparing(String::length).thenComparing(String::compareTo)`. Finally, we collect the results back to a list.

This solution is more concise and readable than the previous one.

It's also worth mentioning that the original question stated that the list will always contain strings. If it's possible that the list could contain non-string elements, then you would want to add a check for this at the start of the method and handle it accordingly.

Also, if the lengths of the strings are not consistent, you may want to handle that case as well.

Hope this helps.

A: Here is a more stream-lined solution:

```
public List<String> listSort(List<String> lst) {
    return lst.stream()
            .filter(s -> s.length() % 2 == 0)
            .sorted()
            .collect(Collectors.toList());
}
```

In this solution,