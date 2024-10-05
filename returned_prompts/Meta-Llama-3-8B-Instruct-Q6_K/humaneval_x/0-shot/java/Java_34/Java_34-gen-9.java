    import java.util.*;

    public class Main {
        public static List<Integer> unique(List<Integer> l) {
            Set<Integer> s = new LinkedHashSet<Integer>(l);
            List<Integer> result = new ArrayList<Integer>(s);
            Collections.sort(result);
            return result;
        }

        public static void main(String[] args) {
            List<Integer> l = Arrays.asList(5, 3, 5, 2, 3, 3, 9, 0, 123);
            List<Integer> result = unique(l);
            System.out.println(result);
        }
    }

