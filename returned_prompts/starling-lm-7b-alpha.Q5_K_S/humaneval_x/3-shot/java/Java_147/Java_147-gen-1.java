        int[] array = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            array[i] = i * i - i + 1;
        }
        int result = 0;
        for (int i = 1; i < array.length - 2; i++) {
            for (int j = i + 1; j < array.length - 1; j++) {
                for (int k = j + 1; k < array.length; k++) {
                    if ((array[i] + array[j] + array[k]) % 3 == 0) {
                        result += 1;
                    }
                }
            }
        }
        return result;
    }
}






public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.getMaxTriples(5));
    }
}
```