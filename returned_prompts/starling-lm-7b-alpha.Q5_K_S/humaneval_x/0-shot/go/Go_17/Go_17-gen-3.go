
import (
    "strings"
    "strconv"
)

var music_list []int
var music_note string

music_string = strings.Replace(music_string, "o|", "2|", -1)
music_string = strings.Replace(music_string, ".", "1|", -1)
music_string = strings.Replace(music_string, "o", "4|", -1)
music_string = strings.Replace(music_string, "o|", "4|", -1)

music_list = strings.Split(music_string, "|")

for _, note := range music_list {
    num, _ := strconv.Atoi(note)
    music_list = append(music_list, num)
}

return music_list

}

// This code will fail if the input string contains a note that is not 'o', 'o|', '.', '|', 'o.'

// This code will not work if the input string is not properly formatted.

// This code does not handle the case when there is a trailing or leading white space in the string.

// This code does not handle the case when there are multiple consecutive spaces in the string.

// This code does not handle the case when there are multiple consecutive spaces in the string.

// This code does not handle the case when there are multiple consecutive spaces in the string.

// This code does not handle the case when there are multiple consecutive spaces in the string.

// This code does not handle the case when there are multiple consecutive spaces in the string.

// This code does not handle the case when there are multiple consecutive spaces in the string.

// This code does not handle the case when there are multiple consecutive spaces in the string.

// This code does not handle the case when there are multiple consecutive spaces in the string.

// This code does not handle the case when there are multiple consecutive spaces in the string.

// This code does not handle the case when there are multiple consecutive spaces in the string.

// This code does not handle the case when there are multiple consecutive spaces in the string.

// This code does not handle the case when there are multiple consecutive spaces