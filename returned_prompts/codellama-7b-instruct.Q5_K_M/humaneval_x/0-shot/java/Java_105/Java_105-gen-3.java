        List<String> result = new ArrayList<>();
        for (Integer i : arr) {
            if (i >= 1 && i <= 9) {
                result.add(i.toString());
            }
        }
        Collections.sort(result);
        Collections.reverse(result);
        return result;
    }
}


B:
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<String> result = new ArrayList<String>();
        for (int i: arr) {
            if (i > 0 && i < 10) {
                result.add(String.valueOf(i));
            }
        }
        Collections.sort(result, Collections.reverseOrder());
        return result;
    }
}


C:
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<String> result = new ArrayList<>();
        for (Integer i : arr) {
            if (i >= 1 && i <= 9) {
                result.add(i.toString());
            }
        }
        Collections.sort(result);
        Collections.reverse(result);
        return result;
    }
}


D:
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<String> result = new ArrayList<>();
        for (Integer i : arr) {
            if (i > 0 && i < 10) {
                result.add(String.valueOf(i));
            }
        }
        Collections.sort(result, Collections.reverseOrder());
        return result;
    }
}


E:
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<String> result = new ArrayList<>();
        for (Integer i : arr) {
            if (i >= 1 && i <= 9)