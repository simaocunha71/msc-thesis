        int sum = 0;
        for (Object o: lst) {
            if (o instanceof Integer) {
                int i = (int) o;
                if (i % 2 == 1) {
                    sum += i * i;
                }
            }
        }
        return sum;
    }
}

public class Test {

    public static void main(String[] args) {
        Test t = new Test();
    }

}


```

```

```