import java.util.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        boolean[] isEven = new boolean[lst1.size()];
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 == 0) {
                isEven[i] = true;
            }
        }
        for (int i = 0; i < lst2.size(); i++) {
            if (isEven[i]) {
                return "NO";
            }
        }
        return "YES";
    }
}


B:
import java.util.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        List<Integer> evenList = new ArrayList<Integer>();
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 == 0) {
                evenList.add(lst1.get(i));
            }
        }
        if (evenList.size() == lst1.size()) {
            return "YES";
        }
        for (int i = 0; i < lst2.size(); i++) {
            if (lst2.get(i) % 2 == 0) {
                return "NO";
            }
        }
        return "YES";
    }
}


C:
import java.util.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        List<Integer> evenList = new ArrayList<Integer>();
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 == 0) {
                evenList.add(lst1.get(i));
            }
        }
        if (evenList.size() == lst1.size()) {
            return "YES";
        }
        for (int i = 0; i < lst2.size(); i++) {
           