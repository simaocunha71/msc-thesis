
	// First, let's sort the sides of the triangle in ascending order.
	sort.Ints([]int{a, b, c})

	// Now, we know that the square of the hypotenuse is equal to the sum of the
	// squares of the other two sides. This is the property of a right-angled triangle.
	// So, we can check this property.
	return a*a+b*b == c*c
}
package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"
	"os"
)

var (
	port     = flag.String("port", "8080", "Port to serve on")
	directory = flag.String("dir", ".", "Directory to serve files from")
)

func main() {
	flag.Parse()

	http.Handle("/", http.FileServer(http.Dir(*directory)))

	log.Printf("Serving %s on HTTP port: %s\n", *directory, *port)
	log.Fatal(http.ListenAndServe(":"+*port, nil))
}

func usage() {
	fmt.Fprintf(os.Stderr, "Usage: %s [options]\n", os.Args[0])
	fmt.Fprintf(os.Stderr, "\nOptions:\n")
	flag.PrintDefaults()
	os.Exit(2)
}


// go run main.go --dir=./static --port=8080
// go run main.go --dir=./static --port=8081
// go run main.go --dir=./static --port=8082

// To build: go build -o static-server
// To run: ./static-server --dir=./static --port=8080
// To run on different ports: ./static-server --dir=./static --port=8081
// To run on different directories: ./static-server --dir=./another-directory --port=8080

// If you want to run multiple servers on different directories and ports, you can run multiple instances of the server with different flags. For example, to run three