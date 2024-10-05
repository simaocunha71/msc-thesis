	return ""
}

func TestSolve(t *testing.T) {
	if Solve("1234") != "4321" {
		t.Errorf("Solve(\"1234\") = %v; want \"4321\"", Solve("1234"))
	}
	if Solve("ab") != "AB" {
		t.Errorf("Solve(\"ab\") = %v; want \"AB\"", Solve("ab"))
	}
	if Solve("#a@C") != "#A@c" {
		t.Errorf("Solve(\"#a@C\") = %v; want \"#A@c\"", Solve("#a@C"))
	}
}
