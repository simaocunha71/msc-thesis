        List<Integer> list = new ArrayList<Integer>(l);
        List<Integer> temp = new ArrayList<Integer>();

        for(int i = 0; i < l.size(); i++) {
            if(i % 3 == 0) {
                temp.add(l.get(i));
            }
        }

        Collections.sort(temp);

        int j = 0;
        for(int i = 0; i < l.size(); i++) {
            if(i % 3 == 0) {
                list.set(i, temp.get(j++));
            }
        }

        return list;
    }
}

This code takes the list, creates a temporary list of the elements at the indices that are divisible by 3, sorts that list, and replaces the original elements at those indices with the sorted values.

The time complexity of the solution is O(n log n), where n is the size of the list, because of the sorting operation. The space complexity is O(n) because we are creating a new list that is the same size as the original list.

The code passes all provided test cases.
*/

//Test Cases:
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.sortThird(Arrays.asList(1, 2, 3))); //[1, 2, 3]
        System.out.println(sol.sortThird(Arrays.asList(5, 6, 3, 4, 8, 9, 2))); //[2, 6, 3, 4, 8, 9, 5]
    }
}




































































































