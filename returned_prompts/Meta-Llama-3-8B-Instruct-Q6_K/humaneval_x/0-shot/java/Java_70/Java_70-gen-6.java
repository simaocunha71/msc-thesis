public class Solution {
    public List<Integer> strangeSortList(List<Integer> lst) {
        if(lst.size() == 0) {
            return lst;
        }
        List<Integer> result = new ArrayList<>();
        Collections.sort(lst);
        result.add(lst.get(0));
        lst.remove(0);
        if(lst.size() > 0) {
            lst.sort((a, b) -> Integer.compare(b, a));
            result.add(lst.get(0));
            lst.remove(0);
        }
        while(lst.size() > 0) {
            result.add(lst.get(0));
            lst.remove(0);
            if(lst.size() > 0) {
                lst.sort((a, b) -> Integer.compare(a, b));
                result.add(lst.get(0));
                lst.remove(0);
            }
        }
        return result;
    }
}