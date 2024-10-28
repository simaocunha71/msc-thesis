import java.util.*;

class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for(int a0 = 0; a0 < n; a0++){
            String s = in.next();
            Map<String, Integer> result = histogram(s);
            if (result.size() > 0) {
                for (Map.Entry<String, Integer> entry : result.entrySet()) {
                    System.out.println(entry.getKey() + " " + entry.getValue());
                }
            } else {
                System.out.println("EMPTY");
            }
        }
    }

    private static Map<String, Integer> histogram(String s) {
        Map<String, Integer> map = new HashMap<>();
        String[] tokens = s.split(" ");
        for (String token : tokens) {
            if (map.get(token) != null) {
                map.put(token, map.get(token) + 1);
            } else {
                map.put(token, 1);
            }
        }
        return map;
    }
}
