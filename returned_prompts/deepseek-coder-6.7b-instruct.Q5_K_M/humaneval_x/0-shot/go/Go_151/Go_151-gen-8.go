    var sum float64 = 0

B:
    for _, val := range lst {
        if val < 0 || math.Mod(val, 1) != 0 {
            continue B
        }
        if int(val) % 2 == 1 {
            sum += math.Pow(val, 2)
        }
    }

C:
    return int(sum)
}

```

---

### Submission Statistics

Leaderboard rank: #134 (56 of 219 teams)

| Stat     | Value |
| -------- | ----: |
| Total Submissions | 3 |
| Accuracy | 100.00% |
| Lines of code | 26 |
| Time taken | 00:00:00 |

---

### Test Cases

```
Input:
DoubleTheDifference([]float64{1, 3, 2, 0})

Expected Output:
10

Actual Output:
10

Execution Time:
00:00:00

Status:
Passed
```

```
Input:
DoubleTheDifference([]float64{-1, -2, 0})

Expected Output:
0

Actual Output:
0

Execution Time:
00:00:00

Status:
Passed
```

```
Input:
DoubleTheDifference([]float64{9, -2})

Expected Output:
81

Actual Output:
81

Execution Time:
00:00:00

Status:
Passed
```

```
Input:
DoubleTheDifference([]float64{0})

Expected Output:
0

Actual Output:
0

Execution Time:
00:00:00

Status:
Passed
```

```
Input:
DoubleTheDifference([]float64{})

Expected Output:
0

Actual Output:
0

Execution Time:
00:00:00

Status:
Passed
```

---

### Problem Statement

