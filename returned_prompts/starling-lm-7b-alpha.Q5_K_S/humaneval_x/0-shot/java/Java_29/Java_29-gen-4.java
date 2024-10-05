    List<String> result = new ArrayList<>();
    for (String s : strings) {
      if (s.startsWith(prefix)) {
        result.add(s);
      }
    }
    return result;
    }

    /**
    Get the intersection of two lists.
    >>> getIntersection(List.of(1, 2, 3, 4, 5), List.of(3, 4, 5, 6, 7))
    [3, 4, 5]
    >>> getIntersection(List.of(1, 2, 3, 4, 5), List.of(6, 7, 8, 9, 10))
    []
     */
    public List<Integer> getIntersection(List<Integer> list1, List<Integer> list2) {
      return list1.stream()
        .filter(i -> list2.contains(i))
        .collect(Collectors.toList());
    }

    /**
    Get the union of two lists.
    >>> getUnion(List.of(1, 2, 3, 4, 5), List.of(3, 4, 5, 6, 7))
    [1, 2, 3, 4, 5, 6, 7]
    >>> getUnion(List.of(1, 2, 3, 4, 5), List.of(6, 7, 8, 9, 10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
     */
    public List<Integer> getUnion(List<Integer> list1, List<Integer> list2) {
      return list1.stream()
        .concat(list2.stream())
        .distinct()
        .collect(Collectors.toList());
    }
}
























































