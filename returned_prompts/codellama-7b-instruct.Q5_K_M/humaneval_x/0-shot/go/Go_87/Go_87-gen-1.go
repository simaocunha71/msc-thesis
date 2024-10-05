
var res [][2]int

for i, v := range lst {
	for j := len(v) - 1; j >= 0; j-- {
		if v[j] == x {
			res = append(res, [2]int{i, j})
		}
	}
}

sort.Slice(res, func(i, j int) bool {
	if res[i][0] < res[j][0] {
		return true
	}
	if res[i][0] == res[j][0] {
		return res[i][1] > res[j][1]
	}
	return false
})

return res
