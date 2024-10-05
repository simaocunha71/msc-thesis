    List<String> result = new ArrayList<>();
    for (String str : lst) {
        if (str.length() % 2 == 0) {
            result.add(str);
        }
    }
    Collections.sort(result, new Comparator<String>() {
        public int compare(String s1, String s2) {
            if (s1.length() == s2.length()) {
                return s1.compareTo(s2);
            } else {
                return Integer.compare(s1.length(), s2.length());
            }
        }
    });
    return result;
}
// The unit test:
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<String> lst1 = Arrays.asList("aa", "a", "aaa");
        List<String> result1 = solution.listSort(lst1);
        System.out.println(result1); // expected output: ["aa"]

        List<String> lst2 = Arrays.asList("ab", "a", "aaa", "cd");
        List<String> result2 = solution.listSort(lst2);
        System.out.println(result2); // expected output: ["ab", "cd"]
    }
}  // expected output: ["aa", "aaa"]



