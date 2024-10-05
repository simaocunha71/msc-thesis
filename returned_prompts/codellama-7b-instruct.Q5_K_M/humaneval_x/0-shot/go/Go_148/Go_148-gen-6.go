
	planets := make(map[string]int)
	planets["Mercury"] = 1
	planets["Venus"] = 2
	planets["Earth"] = 3
	planets["Mars"] = 4
	planets["Jupiter"] = 5
	planets["Saturn"] = 6
	planets["Uranus"] = 7
	planets["Neptune"] = 8

	if planet1 == "" || planet2 == "" {
		return []string{}
	}
	if _, ok := planets[planet1]; !ok {
		return []string{}
	}
	if _, ok := planets[planet2]; !ok {
		return []string{}
	}

	planet1pos := planets[planet1]
	planet2pos := planets[planet2]

	if planet1pos < planet2pos {
		planetslice := []string{}
		for _, v := range planets {
			if v >= planet1pos && v <= planet2pos {
				planetslice = append(planetslice, v)
			}
		}
		return planetslice
	}

	return []string{}
}