        List<Integer> sorted = new ArrayList<>(arr);
        Collections.sort(sorted);
        int index = arr.indexOf(sorted.get(0));
        return index == arr.size() - 1;
    }
}