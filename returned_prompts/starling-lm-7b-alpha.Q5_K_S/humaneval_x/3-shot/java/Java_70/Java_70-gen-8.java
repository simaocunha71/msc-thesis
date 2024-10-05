        List<Integer> result = new ArrayList<>();
        Set<Integer> remaining = new HashSet<>(lst);

        while (remaining.size() > 0) {
            Integer min = Collections.min(remaining);
            result.add(min);
            remaining.remove(min);
            Integer max = Collections.max(remaining);
            result.add(max);
            remaining.remove(max);
        }
        return result;
    }
}

public class _0000_Solutions {
}

```