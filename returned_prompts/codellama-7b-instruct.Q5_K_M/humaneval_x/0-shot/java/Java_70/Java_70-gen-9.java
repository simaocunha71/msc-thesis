
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public static List<Integer> strangeSort(List<Integer> lst) {
        if (lst.size() == 0) {
            return new ArrayList<>();
        }

        int min = Collections.min(lst);
        lst.remove(min);

        int max = Collections.max(lst);
        lst.remove(max);

