public List<List<Integer>> getRow(List<List<Integer>> lst, int x) {
    List<List<Integer>> ans = new ArrayList<List<Integer>>();
    for (int i = 0; i < lst.size(); i++) {
        List<Integer> row = lst.get(i);
        for (int j = row.size() - 1; j >= 0; j--) {
            if (row.get(j) == x) {
                List<Integer> coordinate = new ArrayList<Integer>();
                coordinate.add(i);
                coordinate.add(j);
                ans.add(coordinate);
            }
        }
    }
    return ans;
}