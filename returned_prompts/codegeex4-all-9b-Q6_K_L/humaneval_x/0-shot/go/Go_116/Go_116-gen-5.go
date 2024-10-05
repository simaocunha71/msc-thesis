```go
package kata

func SortArray(arr []int) []int {
    sort.Slice(arr, func(i, j int) bool {
        onesI := bits.OnesCount(uint(arr[i]))
        onesJ := bits.OnesCount(uint(arr[j]))
        if onesI != onesJ {
            return onesI < onesJ
        }
        return arr[i] < arr[j]
    })
    return arr
}
```
B:
```go
package kata

import (
	"sort"
)

func SortArray(arr []int) []int {
	sort.Slice(arr, func(i, j int) bool {
		onesI := bits.OnesCount(uint(arr[i]))
		onesJ := bits.OnesCount(uint(arr[j]))
		if onesI != onesJ {
			return onesI < onesJ
		}
		return arr[i] < arr[j]
	})
	return arr
}
```
C:
```go
package kata

import (
	"sort"
	"math/bits"
)

func SortArray(arr []int) []int {
	sort.Slice(arr, func(i, j int) bool {
		onesI := bits.OnesCount(uint(arr[i]))
		onesJ := bits.OnesCount(uint(arr[j]))
		if onesI != onesJ {
			return onesI < onesJ
		}
		return arr[i] < arr[j]
	})
	return arr
}
```
D:
```go
package kata

import (
	"sort"
	"math/bits"
)

func SortArray(arr []int) []int {
	sort.Slice(arr, func(i, j int) bool {
		onesI := bits.OnesCount(uint(arr[i]))
		onesJ := bits.OnesCount(uint(arr[j]))
		if onesI != onesJ {
			return onesI < onesJ
		}
		return arr[i] < arr[j]
	})
	return arr
}
```
E:
```go
package kata

import (
	"sort"
	"math/bits"
)

func SortArray(arr []int) []int {
	sort.Slice(arr, func(i, j int) bool {
		onesI := bits.OnesCount(uint(arr[i]))
		onesJ := bits.OnesCount(uint(arr[j]))
		if onesI != onesJ {
			return onesI < onesJ
		}
		return arr[i] < arr[j]
	})
	return arr
}
```
F:
```go
package kata

import (
	"