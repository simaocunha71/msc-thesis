
First of all, you should use the defer keyword to close your file after reading. It's better to use the ioutil package instead of os to read the file. It's also better to use a buffer instead of a slice to read the file. You can use bufio.NewReader to achieve this.
import (
    "bufio"
    "fmt"
    "io/ioutil"
    "log"
    "os"
    "strconv"
    "strings"
)

// Given a file path, return a list of strings, each string is a line in the file
func ReadFileLines(filename string) ([]string, error) {
    file, err := os.Open(filename)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    var lines []string
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
    if err := scanner.Err(); err != nil {
        return nil, err
    }

    return lines, nil
}

// Given a string, return a list of strings, each string is a number
func StringToNumbers(s string) []int {
    var numbers []int
    for _, num := range strings.Split(s, " ") {
        if num != "" {
            n, err := strconv.Atoi(num)
            if err != nil {
                log.Println("Invalid number:", num)
            } else {
                numbers = append(numbers, n)
            }
        }
    }
    return numbers
}

// Given a list of numbers, return the index of the maximum number
func MaxIndex(numbers []int) int {
    maxIndex := 0
    for i, num := range numbers {
        if num > numbers[maxIndex] {
            maxIndex = i
        }
    }
    return maxIndex
}

// Given a list of numbers, return the index of the maximum number
func MaxIndex(numbers []int) int {
    maxIndex := 0
    for i, num := range numbers {
        if num > numbers[maxIndex] {
            maxIndex = i
        }
    }
