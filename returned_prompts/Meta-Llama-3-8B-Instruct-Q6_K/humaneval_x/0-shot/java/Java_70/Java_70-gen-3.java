    public List<Integer> strangeSortList(List<Integer> lst) {
        if (lst.isEmpty()) {
            return lst;
        }

        List<Integer> result = new ArrayList<>();
        List<Integer> minMaxList = new ArrayList<>();
        Collections.sort(lst);
        minMaxList.add(lst.get(0));
        minMaxList.add(lst.get(lst.size() - 1));
        lst.remove(0);
        lst.remove(lst.size() - 1);
        result.add(minMaxList.get(0));
        result.add(minMaxList.get(1));
        while (!lst.isEmpty()) {
            minMaxList.clear();
            minMaxList.add(Collections.min(lst));
            minMaxList.add(Collections.max(lst));
            lst.remove(Collections.min(lst));
            lst.remove(Collections.max(lst));
            result.add(minMaxList.get(0));
            result.add(minMaxList.get(1));
        }
        return result;
    }A: 
    public List<Integer> strangeSortList(List<Integer> lst) {
        if (lst.isEmpty()) {
            return lst;
        }

        List<Integer> result = new ArrayList<>();
        List<Integer> minMaxList = new ArrayList<>();
        Collections.sort(lst);
        minMaxList.add(lst.get(0));
        minMaxList.add(lst.get(lst.size() - 1));
        lst.remove(0);
        lst.remove(lst.size() - 1);
        result.add(minMaxList.get(0));
        result.add(minMaxList.get(1));
        while (!lst.isEmpty()) {
            minMaxList.clear();
            minMaxList.add(Collections.min(lst));
            minMaxList.add(Collections.max(lst));
            lst.remove(Collections.min(lst));
            lst.remove(Collections.max(lst));
            result.add(minMaxList.get(0));
            result.add(minMaxList.get(1));
        }
        return result;
    }

