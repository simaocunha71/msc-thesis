    public List<Integer> unique(List<Integer> l) {
        Set<Integer> uniqueSet = new LinkedHashSet<Integer>(l);
        List<Integer> uniqueList = new ArrayList<Integer>(uniqueSet);
        Collections.sort(uniqueList);
        return uniqueList;
    }
}A
