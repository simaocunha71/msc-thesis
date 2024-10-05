    public List<Integer> strangeSortList(List<Integer> lst) {
        if(lst.size() == 0) {
            return lst;
        }
        
        Collections.sort(lst);
        
        List<Integer> result = new ArrayList<>();
        boolean isMin = true;
        
        while(!lst.isEmpty()) {
            if(isMin) {
                result.add(lst.get(0));
                lst.remove(0);
            } else {
                result.add(lst.get(lst.size() - 1));
                lst.remove(lst.size() - 1);
            }
            isMin = !isMin;
        }
        
        return result;
    }
