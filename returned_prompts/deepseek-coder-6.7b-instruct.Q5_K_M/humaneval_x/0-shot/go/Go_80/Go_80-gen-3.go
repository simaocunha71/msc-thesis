
// Your code goes here

}
*/

package main

import "fmt"

func IsHappy(s string) bool {
	if len(s) < 3 {
		return false
	}
	for i := 0; i < len(s)-2; i++ {
		if s[i] == s[i+1] || s[i+1] == s[i+2] || s[i] == s[i+2] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(IsHappy("a"))       // false
	fmt.Println(IsHappy("aa"))      // false
	fmt.Println(IsHappy("abcd"))    // true
	fmt.Println(IsHappy("aabb"))    // false
	fmt.Println(IsHappy("adb"))     // true
	fmt.Println(IsHappy("xyy"))     // false
	fmt.Println(IsHappy("abcabc"))  // true
	fmt.Println(IsHappy("abac"))    // false
	fmt.Println(IsHappy("bcdbcd"))  // true
	fmt.Println(IsHappy("abcdefg")) // true
}
package main

import (
	"github.com/gin-gonic/gin"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
	"github.com/spf13/viper"
	"net/http"
)

type Product struct {
	gorm.Model
	Code  string
	Price uint
}

func main() {
	viper.SetConfigFile("./config.json")
	err := viper.ReadInConfig()
	if err != nil {
		panic(err)
	}
	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})

	r.GET("/products", func(c *