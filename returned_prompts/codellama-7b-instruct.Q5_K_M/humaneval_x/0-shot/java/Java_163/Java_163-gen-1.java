        List<Integer> list = new ArrayList<>();
        for (int i = a; i <= b; i++) {
            if (i % 2 == 0 && i >= 0) {
                list.add(i);
            }
        }
        Collections.sort(list);
        return list;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.generateIntegers(2, 8));
    }
}

