        List<Integer> result = new ArrayList<>();
        l1.removeAll(l2);
        l2.removeAll(l1);
        result.addAll(l1);
        result.addAll(l2);
        result.sort(Comparator.naturalOrder());
        result = new ArrayList<>(new LinkedHashSet<>(result));
        return result;
    }
}

