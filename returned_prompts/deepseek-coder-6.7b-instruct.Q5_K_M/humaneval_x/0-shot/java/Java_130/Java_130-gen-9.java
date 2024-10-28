        List<Integer> list = new ArrayList<>();
        if (n < 0) {
            return list;
        }
        if (n == 0) {
            list.add(3);
            return list;
        }
        if (n == 1) {
            list.add(3);
            list.add(1);
            return list;
        }
        if (n == 2) {
            list.add(3);
            list.add(1);
            list.add(2);
            return list;
        }
        list.add(3);
        list.add(1);
        list.add(2);
        for (int i = 3; i <= n; i++) {
            if (i % 2 == 0) {
                list.add(1 + i / 2);
            } else {
                list.add(list.get(i - 1) + list.get(i - 2) + list.get(i + 1));
            }
        }
        return list;
    }
}


A: The problem is that the last item is getting an index out of bounds error because you are trying to access i + 1th position in the list which doesn't exist yet.
Instead, you should initialize the list with 3 elements and then calculate the rest of the sequence based on these.
Here's the corrected code:
public List<Integer> tri(int n) {
    List<Integer> list = new ArrayList<>();
    if (n < 0) {
        return list;
    }
    if (n >= 0) {
        list.add(3);
    }
    if (n >= 1) {
        list.add(1);
    }
    if (n >= 2) {
        list.add(2);
    }
    for (int i = 3; i <= n; i++) {
        if (i % 2 == 0) {
            list.add(1 + i / 2);
        } else {
            list.add(list.get(i - 1) + list.get(i - 2) + list.get(i - 3));
        }
    }
   