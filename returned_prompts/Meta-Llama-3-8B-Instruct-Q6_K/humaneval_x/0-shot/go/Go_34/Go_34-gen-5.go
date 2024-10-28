Here is a simple Python function that does the same thing:

```python
def Unique(l):
    return sorted(set(l))
```

In this function, we use Python's built-in `set` function to remove duplicates from the list, and then use the `sorted` function to sort the resulting list. This is a very efficient way to do this, as `set` operations are typically very fast in Python.

Here is an example of how you can use this function:

```python
print(Unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This will output:

```
[0, 2, 3, 5, 9, 123]
```

Note: In Python, lists are mutable, so we don't need to use `[]` to create an empty list like we do in Java. We can simply use the `set` function to create a set from the list, and then convert that set back to a list using the `list` function. This is a very common and idiomatic way to do this in Python. 

If you want to do this in Java, you can use a similar approach:

```java
import java.util.*;

public class Main {
    public static int[] Unique(int[] l) {
        Set<Integer> set = new HashSet<>();
        for (int i : l) {
            set.add(i);
        }
        int[] result = new int[set.size()];
        int i = 0;
        for (int j : set) {
            result[i++] = j;
        }
        Arrays.sort(result);
        return result;
    }

    public static void main(String[] args) {
        int[] l = {5, 3, 5, 2, 3, 3, 9, 0, 123};
        int[] result = Unique(l);
        for (int j : result) {
            System.out.print(j + " ");
        }
    }
}
```

This will output:

```
0 2 3 5 9 123
```



Here is a Java function that does the same thing:

```java
import java.util.*;

public class Main {
    public static int[] Unique(int[] l) {
        Set<Integer> set = new HashSet<>();
        for (int i : l) {
            set.add(i);
        }
        int[] result = new int[set.size()];
        int i