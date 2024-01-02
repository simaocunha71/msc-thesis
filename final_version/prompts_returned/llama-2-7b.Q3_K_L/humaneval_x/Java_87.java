import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of lists, [[x1, y1], [x2, y2] ...] such that
    each list is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.

    Examples:
    getRow([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [[0, 0], [1, 4], [1, 0], [2, 5], [2, 0]]
    getRow([], 1) == []
    getRow([[], [1], [1, 2, 3]], 3) == [[2, 2]]
     */
    public List<List<Integer>> getRow(List<List<Integer>> lst, int x) {
        // sort coordinates initially by rows in ascending order.
        Collections.sort(lst, (a1, a2) -> Collections.reverseOrder(a1).compareTo(a2));
        
        List<List<Integer>> output = new ArrayList<>();
        for(int i=0;i<lst.size();i++) {
            // sort coordinates of the row by columns in descending order.
            Collections.sort(lst.get(i), (a1, a2) -> Collections.reverseOrder(a1).compareTo(a2));
            int col = lst.get(i).size();
            
            for(int j=0;j<col;j++) {
                output.add(lst.get(i).subList((j+1), (j+1)+x) == null ? new ArrayList() : lst.get(i).subList((j