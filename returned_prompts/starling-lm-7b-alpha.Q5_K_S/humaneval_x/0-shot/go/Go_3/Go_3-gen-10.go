
    var balance int
    for _, op := range operations {
        balance += op
        if balance < 0 {
            return true
        }
    }
    return false
}

// The function BelowZero takes a slice of integers as an argument. It initializes a variable
// called balance to zero. It then loops through each element of the slice using a for loop.
// For each element, it adds that element to the balance. If at any point the balance becomes
// less than zero, it immediately returns true. If it loops through all the elements and the
// balance never falls below zero, it returns false.

// The loop iterates over the elements of the input slice using a for loop. It uses the blank
// identifier _, which means we don’t care about the value of the element. The range function
// passes each element of the input slice to the loop body one at a time. Inside the loop body,
// we add the current element to the balance.

// We then check if the balance is less than zero. If it is, that means the balance fell below
// zero at some point, so we return true. If the loop finishes without finding a balance below
// zero, we return false.

In the example test cases, BelowZero([]int{1, 2, 3}) returns false because the balance never falls below zero. BelowZero([]int{1, 2, -4, 5}) returns true because the balance falls below zero when we add -4 to the balance.

To test the function, you can use the go test command in the terminal to run the test cases. Here is an example:

$ go test
ok  	_/tmp/test000000 0.007s

The output tells us that the test passed and the time it took to run the tests.

To create a new test case, you can add a new function with the TestXXX prefix. For example, you can create a test case called TestBelowZeroWithNegatives that tests the function with a slice containing negative numbers:

func TestBelowZeroWithNegatives(t *testing.T) {
	tests := []struct {
		operations []int
		expected   bool
	}{
		{operations: []int{1, 