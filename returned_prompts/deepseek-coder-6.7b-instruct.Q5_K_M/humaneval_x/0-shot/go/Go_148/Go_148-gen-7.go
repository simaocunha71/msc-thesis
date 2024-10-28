
    planets := [8]string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

    var (
        index1, index2 int
        present1, present2 bool
    )

    for i, v := range planets {
        if v == planet1 {
            index1, present1 = i, true
        }
        if v == planet2 {
            index2, present2 = i, true
        }
    }

    if !(present1 && present2) {
        return []string{}
    }

    if index1 > index2 {
        index1, index2 = index2, index1
    }

    return planets[index1+1 : index2]
}

*/

import "strings"

func Bf(planet1, planet2 string) (result []string) {

	planets := [8]string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

	index1, index2 := -1, -1

	for i, v := range planets {
		if v == planet1 {
			index1 = i
		} else if v == planet2 {
			index2 = i
		}
	}

	if index1 == -1 || index2 == -1 {
		return []string{}
	}

	if index1 > index2 {
		index1, index2 = index2, index1
	}

	return planets[index1+1 : index2]
}

func main() {
	fmt.Println(Bf("Jupiter", "Neptune"))
	fmt.Println(Bf("Earth", "Mercury"))
	fmt.Println(Bf("Mercury", "Uranus"))
}

// 输出:
// [Saturn Uranus]
// [Venus]
// [Venus Earth Mars Jupiter Saturn]

// 输出结果与预期一致。
// 该函数通过迭代地检查每个