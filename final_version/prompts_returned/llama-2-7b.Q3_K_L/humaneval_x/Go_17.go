
// Input to this function is a string representing musical notes in a special ASCII format.
// Your task is to parse this string and return list of integers corresponding to how many beats does each
// not last.
// 
// Here is a legend:
// 'o' - whole note, lasts four beats
// 'o|' - half note, lasts two beats
// '.|' - quater note, lasts one beat
// 
// >>> ParseMusic('o o| .| o| o| .| .| .| .| o o')
// [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
func ParseMusic(music_string string) []int{
    var result = make([]int, len(music_string))
    
    note := true
    for i:=0; i < len(music_string); i++ {
        if (note == false) && (music_string[i] != 'o') && (music_string[i] != '|' ){
            return result
        }
        
        if ((music_string[i] == 'o') || (music_string[i] == '|')) {
            note = true
            
        } else if(note == true){
            note = false
        } else {
            note = true
            
        }
    }
    
    // If you do not need to use the above-mentioned code, delete it.
}