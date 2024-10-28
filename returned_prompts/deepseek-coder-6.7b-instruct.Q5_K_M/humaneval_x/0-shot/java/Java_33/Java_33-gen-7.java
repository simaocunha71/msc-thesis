        List<Integer> newList = new ArrayList<Integer>(l);
        List<Integer> tempList = new ArrayList<Integer>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                tempList.add(l.get(i));
            }
        }
        Collections.sort(tempList);
        for (int i = 0, j = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                newList.set(i, tempList.get(j++));
            }
        }
        return newList;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.sortThird(Arrays.asList(1, 2, 3)));
        System.out.println(solution.sortThird(Arrays.asList(5, 6, 3, 4, 8, 9, 2)));
    }
}

This Java code takes a list, creates a new list that is a copy of the original list, and then iterates through the original list to find the numbers at indicies divisible by three. It then sorts these numbers and replaces the numbers at the corresponding indices in the new list with the sorted numbers.
*/

//