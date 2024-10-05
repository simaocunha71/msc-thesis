        List<Integer> result = new ArrayList<>();
        Set<Integer> set_l1 = new HashSet<>(l1);
        Set<Integer> set_l2 = new HashSet<>(l2);

        set_l1.retainAll(set_l2);
        result.addAll(set_l1);
        Collections.sort(result);
        return result;
    }
}

