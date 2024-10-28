package main

import "fmt"

func ParseMusic(music_string string) []int {
    var music []int
    for _, s := range music_string {
        switch s {
        case 'o':
            music = append(music, 4)
        case '|':
            music = append(music, 2)
        case '.':
            music = append(music, 1)
        }
    }
    return music
}

func main() {
    fmt.Println(ParseMusic("o o| .| o| o| .| .| .| .| o o"))
}

This is the Go solution for your problem. I have used a switch case to check the character and append the corresponding values. I have assumed that the input string will only have the characters 'o', '.', and '|'. If there are other characters, you can extend the switch case to handle them.