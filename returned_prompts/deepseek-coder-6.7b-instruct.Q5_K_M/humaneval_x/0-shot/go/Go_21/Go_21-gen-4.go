
	min := math.Min(numbers...)
	max := math.Max(numbers...)

	rescaled := make([]float64, len(numbers))
	for i, num := range numbers {
		rescaled[i] = (num - min) / (max - min)
	}
	return rescaled
}

*/

func RescaleToUnit(numbers []float64) []float64 {
	min := numbers[0]
	max := numbers[0]

	for _, num := range numbers {
		if num < min {
			min = num
		}
		if num > max {
			max = num
		}
	}

	rescaled := make([]float64, len(numbers))
	for i, num := range numbers {
		rescaled[i] = (num - min) / (max - min)
	}
	return rescaled
}

func main() {
	nums := []float64{1.0, 2.0, 3.0, 4.0, 5.0}
	fmt.Println(RescaleToUnit(nums))
}

/*
Output:

[0 0.25 0.5 0.75 1]

*/

// END OMIT
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"

	"github.com/gorilla/mux"
)

// Item is a structure for item
type Item struct {
	ID          string `json:"ID"`
	Name        string `json:"Name"`
	Description string `json:"Description"`
	Price       string `json:"Price"`
}

var Items []Item

func homePage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Welcome to the HomePage")
	fmt.Println("Endpoint Hit: homePage")
}

func getItems(w http.ResponseWriter, r *http