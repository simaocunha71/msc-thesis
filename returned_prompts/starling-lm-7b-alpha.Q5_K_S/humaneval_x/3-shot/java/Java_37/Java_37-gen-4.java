        List<Integer> result = new ArrayList<>();
        List<Integer> l_even = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) result.add(l.get(i));
            else l_even.add(l.get(i));
        }
        Collections.sort(l_even);
        for (int i = 0; i < result.size(); i++) {
            if (i % 2 == 0) result.add(l_even.get(i / 2));
        }
        return result;
    }
}

public class _7 {
}
```