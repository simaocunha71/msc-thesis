    Map<String, Integer> map = new HashMap<>();

    for (int i = 0; i < test.length(); i++) {
        char c = test.charAt(i);
        if (map.containsKey(String.valueOf(c))) {
            map.put(String.valueOf(c), map.get(String.valueOf(c)) + 1);
        } else {
            map.put(String.valueOf(c), 1);
        }
    }

    Map<String, Integer> result = new HashMap<>();
    int max = 0;
    for (String s : map.keySet()) {
        if (map.get(s) > max) {
            max = map.get(s);
            result.clear();
            result.put(s, max);
        } else if (map.get(s) == max) {
            result.put(s, map.get(s));
        }
    }
    return result;
    }
}










































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