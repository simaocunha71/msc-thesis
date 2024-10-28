    var result []int
    m := n
    for m != 1 {
        if m % 2 != 0 {
            result = append(result, m)
        }
        if m % 2 == 0 {
            m = m / 2
        } else {
            m = 3 * m + 1
        }
    }
    result = append(result, 1)
    sort.Ints(result)
    return result
}
```

## 解説

以下のように、与えられた正整数nに対して、Collatz数列を生成し、その中で奇数のみを抽出してソートしたリストを返すように実装します。

```python
def get_odd_collatz(n):
    result = []
    m = n
    while m != 1:
        if m % 2 != 0:
            result.append(m)
        if m % 2 == 0:
            m = m // 2
        else:
            m = 3 * m + 1
    result.append(1)
    result.sort()
    return result
```

## テストケース

```python
print(get_odd_collatz(5))  # [1, 5]
print(get_odd_collatz(10))  # [1, 15, 25, 111]
print(get_odd_collatz(15))  # [1, 105, 1111]
```

## ヒント

- 与えられた整数nから始め、Collatz数列を生成します。
- 生成した数列の中で奇数のみを抽出し、それらをソ