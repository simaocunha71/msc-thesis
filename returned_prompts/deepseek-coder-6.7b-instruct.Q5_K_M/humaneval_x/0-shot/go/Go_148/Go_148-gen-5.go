
	planets_order := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
	planet1_index, planet2_index := -1, -1

	for i, planet := range planets_order {
		if planet == planet1 {
			planet1_index = i
		} else if planet == planet2 {
			planet2_index = i
		}
		if planet1_index != -1 && planet2_index != -1 {
			break
		}
	}

	if planet1_index == -1 || planet2_index == -1 {
		return []string{}
	}

	if planet1_index > planet2_index {
		planet1_index, planet2_index = planet2_index, planet1_index
	}

	return planets_order[planet1_index+1 : planet2_index]
}

func main() {
	fmt.Println(Bf("Jupiter", "Neptune")) //==> “Saturn", "Uranus"
	fmt.Println(Bf("Earth", "Mercury"))   //==> "Venus"
	fmt.Println(Bf("Mercury", "Uranus")) //==> "Venus", "Earth", "Mars", "Jupiter", "Saturn"
}

// 