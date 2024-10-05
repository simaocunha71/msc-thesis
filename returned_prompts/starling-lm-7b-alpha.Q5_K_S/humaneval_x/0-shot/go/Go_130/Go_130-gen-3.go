
var res []float64
res = make([]float64, n + 1)
res[0] = 1
res[1] = 3
res[2] = 2

for i := 3; i < n + 1; i++ {
	if i%2 == 0 {
		res[i] = 1 + i/2
	} else {
		res[i] = res[i-1] + res[i-2] + res[i+1]
	}
}
return res

// Another way to do it:
var res []float64
res = append(res, 1)
res = append(res, 3)
res = append(res, 2)

for i := 3; i <= n+1; i++ {
	if i%2 == 0 {
		res = append(res, 1 + i/2)
	} else {
		res = append(res, res[len(res)-1] + res[len(res)-2] + res[len(res)-3])
	}
}
return res

*/

```
  1
  3
  2
  8
  13
  21
  34
  57
  96
  160
  257
  418
  676
  1094
  1771
  2865
  4636
  7502
  12139
  19641
  31781
  51422
  83204
  134626
  217830
  352453
  570288
  922746
  1493032
  2415781
  3908816
  6324598
  10233415
  16558014
  26791429
  43349443
  70140