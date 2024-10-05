    public List<Integer> strangeSortList(List<Integer> lst) {
        if (lst.isEmpty()) {
            return lst;
        }

        Collections.sort(lst);

        List<Integer> result = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();

        while (!lst.isEmpty()) {
            temp.add(lst.get(0));
            lst.remove(0);
            if (!lst.isEmpty()) {
                temp.add(lst.get(lst.size() - 1));
                lst.remove(lst.size() - 1);
            }
            result.addAll(temp);
            temp.clear();
        }

        return result;
    }