
	if n < 2 {
		return y
	}

B:

	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return y
		}
	}

C:

	return x
}

// END OMIT

// Testing
func main() {
	fmt.Println(XOrY(7, 34, 12)) // should return 34
	fmt.Println(XOrY(15, 8, 5))  // should return 5
}

// Testing

```

// END OMIT

// Testing
func main() {
	fmt.Println(XOrY(7, 34, 12)) // should return 34
	fmt.Println(XOrY(15, 8, 5))  // should return 5
}

// Testing

```

// END OMIT

// Testing
func main() {
	fmt.Println(XOrY(7, 34, 12)) // should return 34
	fmt.Println(XOrY(15, 8, 5))  // should return 5
}

// Testing

```

// END OMIT

// Testing
func main() {
	fmt.Println(XOrY(7, 34, 12)) // should return 34
	fmt.Println(XOrY(15, 8, 5))  // should return 5
}

// Testing

```

// END OMIT

// Testing
func main() {
	fmt.Println(XOrY(7, 34, 12)) // should return 34
	fmt.Println(XOrY(15, 8, 5))  // should return 5
}

// Testing

```

// END OMIT

// Testing
func main() {
	fmt.Println(XOrY(7, 34, 12)) // should return 34
	fmt.Println(XOrY(15