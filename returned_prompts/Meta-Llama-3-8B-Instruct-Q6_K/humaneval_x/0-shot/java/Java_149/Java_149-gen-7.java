    public List<String> listSort(List<String> lst) {
        List<String> result = new ArrayList<>();
        for (String s : lst) {
            if (s.length() % 2 == 0) {
                result.add(s);
            }
        }
        Collections.sort(result, (a, b) -> {
            if (a.length() == b.length()) {
                return a.compareTo(b);
            } else {
                return Integer.compare(a.length(), b.length());
            }
        });
        return result;
    }
// Test the function
public static void main(String[] args) {
    Solution solution = new Solution();
    List<String> lst = new ArrayList<>();
    lst.add("aa");
    lst.add("a");
    lst.add("aaa");
    System.out.println(solution.listSort(lst)); // prints ["aa"]
    lst = new ArrayList<>();
    lst.add("ab");
    lst.add("a");
    lst.add("aaa");
    lst.add("cd");
    System.out.println(solution.listSort(lst)); // prints ["ab", "cd"]
}