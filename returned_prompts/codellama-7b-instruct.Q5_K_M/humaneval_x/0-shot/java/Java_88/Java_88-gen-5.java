import java.util.*;

class Solution {
    public int[] sortArray(int[] array) {
        // Write your solution here
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < array.length; i++) {
            list.add(array[i]);
        }
        // Collections.sort(list);
        Collections.sort(list, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                int sum = o1 + o2;
                if (sum % 2 == 0) {
                    return o2 - o1;
                } else {
                    return o1 - o2;
                }
            }
        });

        int[] result = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            result[i] = list.get(i);
        }
        return result;
    }
}

