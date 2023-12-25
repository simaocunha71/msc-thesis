
// Imagine a road that's a perfectly straight infinitely long line.
// n cars are driving left to right;  simultaneously, a different set of n cars
// are driving right to left.   The two sets of cars start out being very far from
// each other.  All cars move in the same speed.  Two cars are said to collide
// when a car that's moving left to right hits a car that's moving right to left.
// However, the cars are infinitely sturdy and strong; as a result, they continue moving
// in their trajectory as if they did not collide.
// 
// This function outputs the number of such collisions.
func CarRaceCollision(n int) int {
    // initialize a list to store the cars.
	arr := [...]int{0, 1}   // arr[0]=0: n-1 empty spaces
	for i := range arr {
        if i == 0 || i == n-1 {
        	arr[i] = len(arr) - 1
        } else {
        	arr[i] = -1   // indicate that the spot is empty
        }
    }
    
    // initialize a list to store the starting times.
	arrTime := make([]int, n+1)
	for i := range arrTime {
    	if i == 0 || i == n-1 {
        	arrTime[i] = -1   // indicate that the spot is empty
        } else {
            arrTime[i] = (n / 2 + 1) * time.Second
        }
    }
	
	var ans int
    
    // a helper function:  for any car and its starting position, return 0 if this isn't a collision, -1 otherwise
	func collide(a []int, b []int){for i := range arr {a[i] = -1}}} func (cars []int) map[*int][]*int{
        m:         make(map[*int]*int),     // map of collisions to the index in cars where this collision occurred
		for i := 0; i < n+1; i++ {
            if _, ok := m[cars[i