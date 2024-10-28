for {
    if len(xs) % 2 != 0 {
        break A
    }
    if xs[len(xs) / 2] == 0 {
        xs = xs[:len(xs) / 2]
    }
    xs[len(xs) / 2] -= 1
}
if xs[0] == 0 {
    xs = xs[1:]
}
for i := 0; i < len(xs) - 1; i++ {
    if xs[i] == 0 {
        xs[i], xs[i+1] = xs[i+1], xs[i]
        break
    }
}
return -1 * float64(xs[0]) / float64(xs[len(xs) - 1])
}



func main() {
	
	xs := []int{1, 2, 3, 4, 5}
	fmt.Println(Poly(xs, 1.1))

	fmt.Println(FindZero([]int{-6, 11, -6, 1}))

}
