
	baseCase0 := 0
	baseCase1 := 0
	baseCase2 := 1

	if n == 0 {
		return baseCase0
	}
	if n == 1 {
		return baseCase1
	}
	if n == 2 {
		return baseCase2
	}

	dp := make([]int, n+1)
	dp[0] = baseCase0
	dp[1] = baseCase1
	dp[2] = baseCase2

	for i := 3; i <= n; i++ {
		dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
	}

	return dp[n]
}

func main() {
	fmt.Println(Fibfib(1)) // 0
	fmt.Println(Fibfib(5)) // 4
	fmt.Println(Fibfib(8)) // 24
}

```

### Java Solution:

```java
public class Main {

    public static int fibFib(int n) {
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 0;
        }
        if (n == 2) {
            return 1;
        }

        int[] dp = new int[n+1];
        dp[0] = 0;
        dp[1] = 0;
        dp[2] = 1;

        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
        }

        return dp[n];
    }

    public static void main(String[] args) {
        System.out.println(fibFib(1)); // 0
        System.out.println(fibFib(5)); // 4
        System.out.println(fibFib(8)); // 24
    }
}
```

### Javascript Solution:

