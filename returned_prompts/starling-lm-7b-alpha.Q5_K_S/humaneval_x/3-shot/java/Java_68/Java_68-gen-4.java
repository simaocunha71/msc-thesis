        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0) {
                result = new ArrayList<>(Arrays.asList(arr.get(i), i));
                break;
            }
        }

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < result.get(0)) {
                result = new ArrayList<>(Arrays.asList(arr.get(i), i));
            } else if (arr.get(i) % 2 == 0 && arr.get(i) == result.get(0) && i < result.get(1)) {
                result = new ArrayList<>(Arrays.asList(arr.get(i), i));
            }
        }
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.pluck(Arrays.asList(4,2,3)));
    }
}

```