
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
	if n <= 0 {
		return 0
	}
	// create a data structure that stores the positions of each car at every moment in time and their indices (which are equal to their position).
	carMap := make(map[int][]int, n)
	for i:=1;i<=n/2;i++ {
		newCar := make([]int, 0, 5)
		for _, val := range carMap[i-1] {
			if val >= 2 {
				newCar = append(newCar, val+1)
			} else {
				carMap[val][0] = i;
				for _, v := range carMap[i-1] {
					if v < 2 {
						newCar = append(newCar, v+1)
					} else {
						carMap[v][0] = i;
					}
				}
			}
		}
		for idx := len(newCar);idx < 5;idx++ {
			if newCar[len(newCar)-1-idx+i] >= 2 {
				newCar = append(newCar, newCar[len(newCar)-1-idx+i]+1)
			} else {
				carMap[newCar[