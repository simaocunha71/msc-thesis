        Set<Integer> set1 = new HashSet<Integer>(l1);
        Set<Integer> set2 = new HashSet<Integer>(l2);

        set1.retainAll(set2);

        List<Integer> result = new ArrayList<Integer>(set1);
        Collections.sort(result);
        return result;
    }
}

