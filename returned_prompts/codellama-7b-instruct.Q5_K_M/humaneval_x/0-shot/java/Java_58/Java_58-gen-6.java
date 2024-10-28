        Set<Integer> s1 = new HashSet<>(l1);
        Set<Integer> s2 = new HashSet<>(l2);
        Set<Integer> s3 = new HashSet<>(s1);
        s3.retainAll(s2);
        List<Integer> l3 = new ArrayList<>(s3);
        Collections.sort(l3);
        return l3;
    }
}
