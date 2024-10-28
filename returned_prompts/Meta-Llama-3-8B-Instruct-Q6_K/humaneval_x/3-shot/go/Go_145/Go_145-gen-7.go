    type Point struct {
        num int
        sum int
        index int
    }

    points := make([]Point, len(nums))
    for i, num := range nums {
        sum := 0
        for _, c := range strconv.Itoa(num) {
            sum += int(c - '0')
        }
        points[i] = Point{num, sum, i}
    }

    sort.Slice(points, func(i, j int) bool {
        if points[i].sum != points[j].sum {
            return points[i].sum < points[j].sum
        }
        return points[i].index < points[j].index
    })

    result := make([]int, len(points))
    for i, p := range points {
        result[i] = p.num
    }
    return result
}
}  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  } 