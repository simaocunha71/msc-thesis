	apple_or_orange := strings.Fields(s)
	apples, _ := strconv.Atoi(apple_or_orange[0])
	oranges, _ := strconv.Atoi(apple_or_orange[2])

	
B:
	total_fruits := n - apples - oranges
	
C:
	return total_fruits
}

*/

package main

import (
	"fmt"
	"strconv"
	"strings"
)

func FruitDistribution(s string, n int) int {

	apple_or_orange := strings.Fields(s)
	apples, _ := strconv.Atoi(apple_or_orange[0])
	oranges, _ := strconv.Atoi(apple_or_orange[2])

	total_fruits := n - apples - oranges

	return total_fruits
}

func main() {
	fmt.Println(FruitDistribution("5 apples and 6 oranges", 19))  //8
	fmt.Println(FruitDistribution("0 apples and 1 oranges", 3))   //2
	fmt.Println(FruitDistribution("2 apples and 3 oranges", 100)) //95
	fmt.Println(FruitDistribution("100 apples and 1 oranges", 120)) //19
}
package main

import (
	"fmt"
	"log"
	"os"
	"strings"

	"github.com/urfave/cli"

	"./internal/app/messenger"
)

func main() {
	app := cli.NewApp()
	app.Name = "chat"
	app.Usage = "CLI Chat"
	app.Version = "0.0.1"

	app.Commands = []cli.Command{
		{
			Name:    "start",
			Aliases: []string{"s"},
			Usage:   "Starts a chat session",
			Action: func(c *cli.Context) error