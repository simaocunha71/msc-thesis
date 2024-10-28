	for _, grade := range grades {
		switch {
		case grade >= 4.0:
			return []string{"A+"}
		case grade >= 3.7:
			return []string{"A"}
		case grade >= 3.3:
			return []string{"A-"}
		case grade >= 3:
			return []string{"B+"}
		case grade >= 2.7:
			return []string{"B"}
		case grade >= 2.3:
			return []string{"B-"}
		case grade >= 2:
			return []string{"C+"}
		case grade >= 1.7:
			return []string{"C"}
		case grade >= 1.3:
			return []string{"C-"}
		case grade >= 1:
			return []string{"D+"}
		case grade >= 0.7:
			return []string{"D"}
		case grade >= 0:
			return []string{"D-"}
		default:
			return []string{"E"}
		}
	}
	return []string{"E"}

}

func main() {

	fmt.Println(NumericalLetterGrade([]float64{4.0, 3, 1.7, 2, 3.5}))
}
