    public List<Integer> strangeSortList(List<Integer> lst) {
        if (lst.size() == 0) {
            return lst;
        }

        List<Integer> result = new ArrayList<>();
        List<Integer> minList = new ArrayList<>();
        List<Integer> maxList = new ArrayList<>();

        for (int i : lst) {
            if (minList.isEmpty() || i < minList.get(0)) {
                minList.clear();
                minList.add(i);
            } else if (i < minList.get(minList.size() - 1)) {
                minList.add(i);
            }

            if (maxList.isEmpty() || i > maxList.get(0)) {
                maxList.clear();
                maxList.add(i);
            } else if (i > maxList.get(maxList.size() - 1)) {
                maxList.add(i);
            }
        }

        while (!minList.isEmpty() || !maxList.isEmpty()) {
            if (!minList.isEmpty()) {
                result.add(minList.get(0));
                minList.remove(0);
            }

            if (!maxList.isEmpty()) {
                result.add(maxList.get(maxList.size() - 1));
                maxList.remove(maxList.size() - 1);
            }
        }

        return result;
    } 

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> lst = new ArrayList<>();
        lst.add(1);
        lst.add(2);
        lst.add(3);
        lst.add(4);
        List<Integer> result = solution.strangeSortList(lst);
        System.out.println(result);
    }
}
