        List<Integer> result = new ArrayList<>();
        Set<Integer> s1 = new HashSet<>(l1);
        Set<Integer> s2 = new HashSet<>(l2);
        s1.retainAll(s2);
        result.addAll(s1);
        return result.stream().sorted().collect(Collectors.toList());
    }
}

