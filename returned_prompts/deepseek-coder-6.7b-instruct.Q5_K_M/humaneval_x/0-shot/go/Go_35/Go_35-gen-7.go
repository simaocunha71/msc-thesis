
	max := l[0]
	for _, value := range l {
		if value > max {
			max = value
		}
	}
	return max
}

*/

package main

import (
	"fmt"
)

func MaxElement(l []int) int {
	max := l[0]
	for _, value := range l {
		if value > max {
			max = value
		}
	}
	return max
}

func main() {
	fmt.Println(MaxElement([]int{1, 2, 3}))
	fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}))
}
package main

import (
	"fmt"
	"net/http"
)

// HandlerFunc is a function that takes in a ResponseWriter and a Request and returns nothing.
type HandlerFunc func(http.ResponseWriter, *http.Request)

// Server is a struct that represents the server.
type Server struct {
	routes map[string]HandlerFunc
}

// NewServer is a function that creates a new Server.
func NewServer() *Server {
	return &Server{
		routes: make(map[string]HandlerFunc),
	}
}

// HandleFunc is a method that adds a new route to the server.
func (s *Server) HandleFunc(path string, handler HandlerFunc) {
	s.routes[path] = handler
}

// ServeHTTP is a method that implements the http.Handler interface.
func (s *Server) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	handler, ok := s.routes[r.URL.Path]
	if !ok {
		http.NotFound(w, r)
		return
	}
	handler(w, r)
}

// HomeHandler is a function that handles the home page.
func HomeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Welcome to our website")
}

