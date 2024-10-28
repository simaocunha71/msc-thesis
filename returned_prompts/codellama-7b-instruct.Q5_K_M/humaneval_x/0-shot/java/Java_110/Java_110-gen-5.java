import java.util.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        if (lst1.isEmpty() || lst2.isEmpty())
            return "NO";

        int count = 0;
        for (int i : lst1)
            if (i % 2 == 0)
                count++;

        if (count == lst1.size())
            return "YES";

        for (int i : lst2)
            if (i % 2 == 0)
                count--;

        return count == 0 ? "YES" : "NO";
    }
}
