    if text == "" {
        return nil
    }
    hasher := md5.New()
    hasher.Write([]byte(text))
    return fmt.Sprintf("%x", hasher.Sum(nil))
}

*/

package main

import (
	"crypto/md5"
	"fmt"
)

func StringToMd5(text string) interface{} {
	if text == "" {
		return nil
	}
	hasher := md5.New()
	hasher.Write([]byte(text))
	return fmt.Sprintf("%x", hasher.Sum(nil))
}

func main() {
	fmt.Println(StringToMd5("Hello world"))
}

/*
This program takes a string as an argument and returns its MD5 hash equivalent as a string.
If the input string is empty, it returns nil.
*/
package main

import (
	"fmt"
	"net"
)

func main() {
	// 指定要连接的服务器
	server := "golang.org:80"

	// 创建一个连接到服务器的TCP连接
	conn, err := net.Dial("tcp", server)
	if err != nil {
		fmt.Printf("连接到服务器 %s 失败: %s\n", server, err)
		return
	}

	// 创建一个HTTP请求
	request := "GET / HTTP/1.1\r\nHost: " + server + "\r\n\r\n"

	// 将请求写入连接
	_, err = fmt.Fprintf(conn, request)
	if err != nil {
		fmt.Printf("写入连接失败: %s\n", err)
		return
	}

	// 创建一个缓冲区，用于读取响应
	buffer := make([]byte, 1024)

	// 读取响应
	for {
		n, err := conn.Read(buffer)
		if err != nil {
			fmt.Printf("读取响应失败: %s\n", err)
			return