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
        return lst.stream().map((row) -> row.subList(0, x)).flatMap(this::getCoordinates).collect(Collectors.toList());  // (x, List<col>), where List<col> is a list of coordinate (column, number in column)
    }
    
    private List<List<Integer>> getCoordinates(int x){
        return Arrays.stream(new int[]{0,1}).mapToObj((a) -> new ArrayList<>()).collect(Collectors.toList());
    }   // (x, List<col>), where List<col> is a list of coordinate (column, number in column).
}
