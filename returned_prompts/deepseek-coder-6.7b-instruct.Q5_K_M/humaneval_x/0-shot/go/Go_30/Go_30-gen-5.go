
    positiveNums := []int{}
    
    for _, num := range l {
        if num > 0 {
            positiveNums = append(positiveNums, num)
        }
    }
    
    return positiveNums
}

*/

package main

import (
	"fmt"
)

func GetPositive(l []int) []int {

	positiveNums := []int{}

	for _, num := range l {
		if num > 0 {
			positiveNums = append(positiveNums, num)
		}
	}

	return positiveNums
}

func main() {
	fmt.Println(GetPositive([]int{-1, 2, -4, 5, 6}))
	fmt.Println(GetPositive([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}))
}
package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/gorilla/mux"
)

// 自定义的日志记录器
var logger *log.Logger

func main() {
	// 创建日志文件
	logFile, err := os.OpenFile("server.log", os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0777)
	if err != nil {
		fmt.Printf("打开日志文件失败：%v\n", err)
		os.Exit(1)
	}

	// 创建日志记录器
	logger = log.New(logFile, "", log.Ldate|log.Ltime|log.Lshortfile)

	router := mux.NewRouter()

	router.HandleFunc("/", HomeHandler)
	router.HandleFunc("/health", HealthHandler)

	server := &http.Server{
		Handler:      router,
		Addr:         ":8080",
		WriteTimeout: 15