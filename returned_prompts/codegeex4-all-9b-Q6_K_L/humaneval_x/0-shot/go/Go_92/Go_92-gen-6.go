You can solve this by creating a function that takes three parameters, x, y, and z. The function should return true if one of the numbers is equal to the sum of the other two, and all numbers are integers. Otherwise, it should return false.

Here is the code:

```swift
func AnyInt(x: Int, y: Int, z: Int) -> Bool {
    if x + y == z || x + z == y || y + z == x {
        return true
    } else {
        return false
    }
}
```

This code checks if the sum of any two numbers is equal to the third number. If it is, it returns true. Otherwise, it returns false. Note that this code assumes that the inputs are integers. If the inputs are not integers, you can modify the code to handle them accordingly.