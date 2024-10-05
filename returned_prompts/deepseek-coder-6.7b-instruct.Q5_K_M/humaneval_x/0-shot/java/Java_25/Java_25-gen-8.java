        List<Integer> factors = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                factors.add(i);
                n /= i;
            }
        }
        return factors;
    }
}

*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.factorize(8)); // [2, 2, 2]
        System.out.println(solution.factorize(25)); // [5, 5]
        System.out.println(solution.factorize(70)); // [2, 5, 7]
    }
}
```

## タスク

- [x] Java の素因数分解プログラムを完成させる。
- [x] 必要に応じてコードを最適化する。
- [x] コードにドキュメントを追加する。

## 学習内容

- 素因数分解の基本的な概念
- Java での素因数分解の実装
- 素因数分解の最適化方法

## 参考文献

- [素因数分解 - Wikipedia](https://ja.wikipedia.org/wiki/%E7%B4%A0%E5%9B%A0%E6%95%B0%E5%88%86%E8%A7%A3)
- [Java の素因数分解プログラム - GeeksforGeeks](https://www.geeksforgeeks.org/java-program-prime-factors/)
- [アルゴリズム - 素因数分解 - コンピュータ