        Collections.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                int c1 = Integer.bitCount(o1);
                int c2 = Integer.bitCount(o2);

                if (c1 == c2) {
                    return o1.compareTo(o2);
                } else {
                    return Integer.compare(c1, c2);
                }
            }
        });

        return arr;
    }
}

This code uses a custom comparator to sort the array. The `Integer.bitCount(o1)` method returns the number of one bits in the binary representation of the integer, and `o1.compareTo(o2)` compares the two integers. The first comparison checks if the number of one bits are the same, if so, it sorts by decimal value, otherwise it sorts by number of one bits.

```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```
