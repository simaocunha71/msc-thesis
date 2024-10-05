import java.util.*;
import java.lang.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int total1 = lst1.stream().mapToInt(s -> s.length()).sum();
        int total2 = lst2.stream().mapToInt(s -> s.length()).sum();
        return total1 < total2 ? lst1 : lst2;
    }
}