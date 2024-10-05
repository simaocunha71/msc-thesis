        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    List<Integer> tmp = new ArrayList<>();
                    tmp.add(i);
                    tmp.add(j);
                    res.add(tmp);
                }
            }
        }
        // Sorting by rows in ascending order and
        // by columns in descending order
        res.sort(Comparator.comparing((List<Integer> o) -> o.get(0)).thenComparing((List<Integer> o) -> o.get(1), Comparator.reverseOrder()));
        return res;
    }
}

Here, we are iterating over the 2D list and checking each element if it is equal to x. If it is, we add the row and column indices to the result list. After that, we sort the result list first by the rows (0-th element of each list) in ascending order and then by the columns (1-st element of each list) in descending order.

The time complexity of this solution is O(n*m) where n is the number of rows and m is the maximum number of columns. This is because we have to go through each element of the 2D list.

The space complexity is O(k), where k is the number of occurrences of x in the 2D list. This is because we are storing the coordinates of x in the result list.

This solution assumes that the 2D list does not contain other lists or collections.
*/

// Java program to demonstrate the working of Comparator.
public class Main {
    public static void main(String[] args)
    {
        List<List<Integer>> lst = new ArrayList<List<Integer>>();
        List<Integer> lst1 = Arrays.asList(1,2,3,4,5,6);
        List<Integer> lst2 = Arrays.asList(1,2,3,4,1,6);
       