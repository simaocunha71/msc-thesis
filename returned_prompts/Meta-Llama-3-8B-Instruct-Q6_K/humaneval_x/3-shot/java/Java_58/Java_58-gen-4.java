        Set<Integer> set1 = new HashSet<>(l1);
        set1.retainAll(new HashSet<>(l2));
        return new ArrayList<>(set1);
    }
}

