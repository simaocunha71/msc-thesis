        List<Integer> result = new ArrayList<>();
        Set<Integer> set1 = new HashSet<>(l1);
        Set<Integer> set2 = new HashSet<>(l2);
        set1.retainAll(set2);
        result.addAll(set1);
        Collections.sort(result);
        return result;
    }
}

