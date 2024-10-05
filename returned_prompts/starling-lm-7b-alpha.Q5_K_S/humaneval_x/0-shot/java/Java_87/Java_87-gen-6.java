        List<List<Integer>> ans = new ArrayList<>();

        for(int i = 0; i < lst.size(); i++) {
            int row = i;
            List<Integer> curr = new ArrayList<>();

            for(int j = 0; j < lst.get(i).size(); j++) {
                if(lst.get(i).get(j) == x) {
                    curr.add(row);
                    curr.add(j);
                    ans.add(curr);
                    continue A;
                }
            }
        }
        Collections.sort(ans, (a, b) -> a.get(0) - b.get(0));
        Collections.sort(ans, (a, b) -> b.get(1) - a.get(1));
        return ans;
    }
}


    */


/*

public class Solution {
    public List<List<Integer>> getRow(List<List<Integer>> lst, int x) {
        List<List<Integer>> res = new ArrayList<>();

        for (List<Integer> row : lst) {
            int index = row.indexOf(x);
            if (index != -1) {
                List<Integer> r = new ArrayList<>();
                r.add(index);
                r.add(row.indexOf(x));
                res.add(r);
            }
        }
        Collections.sort(res, (a, b) -> a.get(0) - b.get(0));
        Collections.sort(res, (a, b) -> b.get(1) - a.get(1));
        return res;
    }
}

*/

/*

public class Solution {
    public List<List<Integer>> getRow(List<List<Integer>> lst, int x) {
        List<List<Integer>> res = new ArrayList<>();

        for (List<Integer> row : lst) {
            int index = row.indexOf(x);
            if (index != -1) {
                List<Integer> r = new ArrayList<>();
                r.add(index);
