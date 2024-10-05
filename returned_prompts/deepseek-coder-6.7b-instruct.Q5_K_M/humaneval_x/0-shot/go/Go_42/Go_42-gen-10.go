
    var result []int
    for _, value := range l {
        result = append(result, value+1)
    }
    return result
}

```


## Swift

```swift
// Return list with elements incremented by 1.
// 
// >>> IncrList([1, 2, 3])
// [2, 3, 4]
// >>> IncrList([5, 3, 5, 2, 3, 3, 9, 0, 123])
// [6, 4, 6, 3, 4, 4, 10, 1, 124]

func IncrList(l: [Int]) -> [Int] {

    var result = [Int]()
    for value in l {
        result.append(value + 1)
    }
    return result
}

```


## VB.net

```vb.net
' Return list with elements incremented by 1.
' >>> IncrList(New List(Of Integer) From {1, 2, 3})
' 2, 3, 4
' >>> IncrList(New List(Of Integer) From {5, 3, 5, 2, 3, 3, 9, 0, 123})
' 6, 4, 6, 3, 4, 4, 10, 1, 124

Function IncrList(l As List(Of Integer)) As List(Of Integer)

    Dim result As New List(Of Integer)
    For Each value As Integer In l
        result.Add(value + 1)
    Next
    Return result
End Function

```


## zkl

```zkl
fcn IncrList(l){ l.apply(fcn(x){ x.inc() }) }  // Increment each element in list.
print(IncrList([1,2,3]));  // Output: [2,3,4]
print(IncrList([5,3,5,2,3,3,9,0,123