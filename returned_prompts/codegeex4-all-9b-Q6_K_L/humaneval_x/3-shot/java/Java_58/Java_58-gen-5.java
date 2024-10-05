        Set<Integer> result = new HashSet<Integer>(l1);
        result.retainAll(l2);
        List<Integer> res = new ArrayList<Integer>(result);
        Collections.sort(res);
        return res;
    }
}

