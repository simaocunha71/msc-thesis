
// Here we will compare each element from the start and end of the array. If they are not equal,
// we will increase the counter by 1. After the loop, the counter will contain the minimum number of changes.

    counter := 0
    for i := 0; i < len(arr)/2; i++ {
        if arr[i] != arr[len(arr)-i-1] {
            counter++
        }
    }

    return counter
}

*/

package main

import (
	"fmt"
)

func SmallestChange(arr []int) int {

	counter := 0
	for i := 0; i < len(arr)/2; i++ {
		if arr[i] != arr[len(arr)-i-1] {
			counter++
		}
	}

	return counter
}

func main() {
	fmt.Println(SmallestChange([]int{1, 2, 3, 5, 4, 7, 9, 6})) // Should print 4
	fmt.Println(SmallestChange([]int{1, 2, 3, 4, 3, 2, 2}))     // Should print 1
	fmt.Println(SmallestChange([]int{1, 2, 3, 2, 1}))            // Should print 0
}
package main

import (
	"fmt"
	"os"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
	"github.com/nicklaw5/helix"
)

var (
	client *helix.Client
)

func main() {
	err := godotenv.Load(".env")

	if err != nil {
		panic("Error loading .env file")
	}

	appClientID := os.Getenv("TWITCH_APP_CLIENT_ID")
	appClientSecret := os.Getenv("TWITCH_APP_CLIENT_SECRET")

	client, err = helix.NewClient(&helix.Options{
