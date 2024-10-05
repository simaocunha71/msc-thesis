    sort.Slice(arr, func(i, j int) bool {
        ib := fmt.Sprintf("%b", arr[i])
        jb := fmt.Sprintf("%b", arr[j])
        ic := len(ib) - len(strings.TrimLeft(ib, "0"))
        jc := len(jb) - len(strings.TrimLeft(jb, "0"))
        if ic == jc {
            return arr[i] < arr[j]
        }
        return ic < jc
    })
    return arr
}
```


## 100 doors problem

The "100 doors" problem is a programming puzzle that originated with a riddle posed by a logician for Usenix, a computer security conference. The problem was first posed (and solved) on April 19, 2009.

You have 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, visit every door and  toggle  the door (if the door is closed, open it; if it is open, close it). The second time, only visit every 2nd door (door #2, #4, #6, ...) and toggle it. The third time, visit every 3rd door (door #3, #6, #9, ...) and toggle it. 

After the last pass, which is 100th pass, you want to know the state of the doors (which are either open or closed). Which doors will be left open?

The answer is that only doors 1, 4, 9, 16, 25, 36, 49, 64, 81, and 100 will be left open. This is because those are the only numbers that have an odd number of factors (including 1 and the number itself). 

For any number n, if it has an odd number of factors, the number of doors that will be left open is the number of its factors.

## Fibonacci sequence

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones.

