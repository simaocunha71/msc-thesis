    int l1 = lst1.size();
    int l2 = lst2.size();
    int c1 = 0, c2 = 0;
    for (int i = 0; i < l1; i++) {
        c1 += lst1.get(i).length();
    }
    for (int i = 0; i < l2; i++) {
        c2 += lst2.get(i).length();
    }
    if (c1 < c2) {
        return lst1;
    } else if (c1 > c2) {
        return lst2;
    } else {
        List<String> res = new ArrayList<>();
        for (int i = 0; i < l1; i++) {
            res.add(lst1.get(i));
        }
        for (int i = 0; i < l2; i++) {
            if (res.size() == l1) {
                break;
            }
            res.add(lst2.get(i));
        }
        return res;
    }
    }
}








```

ANSWER:
```
public List<String> totalMatch(List<String> lst1, List<String> lst2) {

    int l1 = lst1.size();
    int l2 = lst2.size();
    int c1 = 0, c2 = 0;
    for (int i = 0; i < l1; i++) {
        c1 += lst1.get(i).length();
    }
    for (int i = 0; i < l2; i++) {
        c2 += lst2.get(i).length();
    }
    if (c1 < c2) {
        return lst1;
    } else if (c1 > c2) {
        return lst2;
    } else {
        List<String> res = new ArrayList<>();
        for (int i = 0; i < l1; i++) {
            res.add(lst1.get(i));
        }