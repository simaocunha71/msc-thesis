
// I tried to get it done with math.Pow() but I couldn't find a way to do it without
// having to convert x into a string, which I don't think is the most efficient way.
// Also, I tried to do it with recursion and while loops but they didn't work either.
// Is there any way to do this without converting x into a string?

func IsSimplePower(x int, n int) bool {
	if x == 1 {
		return true
	}
	if x == n*n {
		return true
	}
	if x == n*n*n {
		return true
	}
	if x == n*n*n*n {
		return true
	}
	if x == n*n*n*n*n {
		return true
	}
	if x == n*n*n*n*n*n {
		return true
	}
	if x == n*n*n*n*n*n*n {
		return true
	}
	return false
}

func TestIsSimplePower(t *testing.T) {
	if !IsSimplePower(1, 4) {
		t.Error("IsSimplePower(1, 4) = false, want true")
	}
	if !IsSimplePower(2, 2) {
		t.Error("IsSimplePower(2, 2) = false, want true")
	}
	if !IsSimplePower(8, 2) {
		t.Error("IsSimplePower(8, 2) = false, want true")
	}
	if IsSimplePower(3, 2) {
		t.Error("IsSimplePower(3, 2) = true, want false")
	}
	if IsSimplePower(3, 1) {
		t.Error("IsSimplePower(3, 1) = true, want false")
	}
	if IsSimplePower(5, 3) {
		t.Error("IsSimplePower(5, 3) = true, want false")
	}
}

func BenchmarkIsSimplePower(