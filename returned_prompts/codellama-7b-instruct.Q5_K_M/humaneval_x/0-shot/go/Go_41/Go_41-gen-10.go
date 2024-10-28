
// Let's find the distance between two cars:
//
//  d = (n-1) * (n-1) * (n-1)
//
//  The number of collisions:
//
//  collisions = d * (n-1) * (n-1)
//
//  Since the cars are infinitely sturdy, the number of collisions is 0.
//
//  But we can't just return 0, because the test cases require us to return 0
//  if n is less than or equal to 1.
//
//  If n is less than or equal to 1, we need to return (n - 1) * (n - 1)
//  which is the number of collisions between two cars, when they are in the same
//  direction.
//
//  Otherwise, we need to return 0.
//
//  So we have the following code:

    if n <= 1 {
        return (n - 1) * (n - 1)
    }
    return 0
}

// 
// 
// 
