        Set<Integer> s1 = new HashSet<>(l1);
        Set<Integer> s2 = new HashSet<>(l2);
        s1.retainAll(s2);

        List<Integer> result = new ArrayList<>(s1);
        Collections.sort(result);
        return result;
     }
}

