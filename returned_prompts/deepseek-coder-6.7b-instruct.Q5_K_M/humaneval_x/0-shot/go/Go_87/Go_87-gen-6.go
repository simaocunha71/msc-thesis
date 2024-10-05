
	coordinates := [][2]int{}
	for i, row := range lst {
		for j, col := range row {
			if col == x {
				coordinates = append(coordinates, [2]int{i, j})
			}
		}
	}

	sort.Slice(coordinates, func(i, j int) bool {
		if coordinates[i][0] == coordinates[j][0] {
			return coordinates[i][1] > coordinates[j][1]
		}
		return coordinates[i][0] < coordinates[j][0]
	})

	return coordinates
}

```

### JavaScript

```javascript
// You are given a 2 dimensional data, as a nested arrays,
// which is similar to matrix, however, unlike matrices,
// each row may contain a different number of columns.
// Given lst, and integer x, find integers x in the list,
// and return list of tuples, [(x1, y1), (x2, y2) ... ] such that
// each tuple is a coordinate – (row, columns), starting with 0.
// Sort coordinates initially by rows in ascending order.
// Also, sort coordinates of the row by columns in descending order.
// 
// Examples:
// GetRow([
//  [1,2,3,4,5,6],
//  [1,2,3,4,1,6],
//  [1,2,3,4,5,1]
// ], 1) ➞ [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
// GetRow([], 1) ➞ []
// GetRow([[], [1], [1, 2, 3]], 3) ➞ [(2, 2)]

function GetRow(lst, x) {
	let coordinates = [];
	for(let i=0; i<lst.length; i++) {
		for(let j=0; j<lst[i].length; j++) {
			if(lst[i][