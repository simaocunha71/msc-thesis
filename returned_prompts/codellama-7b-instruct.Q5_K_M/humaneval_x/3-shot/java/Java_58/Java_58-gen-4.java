        Set<Integer> set = new HashSet<>(l1);
        set.retainAll(l2);
        List<Integer> result = new ArrayList<>(set);
        result.sort(Comparator.naturalOrder());
        return result;
    }
}

