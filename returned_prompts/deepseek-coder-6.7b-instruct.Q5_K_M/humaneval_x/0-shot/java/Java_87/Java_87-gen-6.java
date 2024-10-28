        List<List<Integer>> res = new ArrayList<>();

        if (lst == null || lst.size() == 0) {
            return res;
        }

        for (int i = 0; i < lst.size(); i++) {
            List<Integer> row = lst.get(i);
            for (int j = 0; j < row.size(); j++) {
                if (row.get(j) == x) {
                    List<Integer> coordinate = new ArrayList<>();
                    coordinate.add(i);
                    coordinate.add(j);
                    res.add(coordinate);
                }
            }
        }

        Collections.sort(res, new Comparator<List<Integer>>() {
            @Override
            public int compare(List<Integer> o1, List<Integer> o2) {
                if (o1.get(0).equals(o2.get(0))) {
                    return o2.get(1) - o1.get(1);
                }
                else {
                    return o1.get(0) - o2.get(0);
                }
            }
        });

        return res;
    }
}


A: You're almost there. You just need to sort the coordinates by rows in ascending order and columns in descending order, following your instructions. Your Comparator correctly handles this. Here it is:

```java
Collections.sort(res, new Comparator<List<Integer>>() {
    @Override
    public int compare(List<Integer> o1, List<Integer> o2) {
        if (o1.get(0).equals(o2.get(0))) {
            return o2.get(1) - o1.get(1);
        } else {
            return o1.get(0) - o2.get(0);
        }
    }
});
```

The first `if` block checks if the rows are the same. If they are, it sorts by columns in descending order. If the rows are different, it sorts by rows in ascending order.

This will return your sorted list of coordinates.

Please also note that