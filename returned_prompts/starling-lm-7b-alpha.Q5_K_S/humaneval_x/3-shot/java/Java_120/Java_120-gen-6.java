        List<Integer> result = new ArrayList<>();
        int max = arr.get(arr.size() - 1);
        result.add(max);
        arr.remove(arr.size() - 1);

        while (result.size() < k) {
            Collections.sort(arr);
            result.add(arr.get(arr.size() - 1));
            arr.remove(arr.size() - 1);
        }
        return result;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
    }
}

```