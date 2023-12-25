
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
	var result []int = make([]int, len(music_string))
    for j:=0;j<len(music_string);j++ {
    	if music_string[j+1:]=="o|" || music_string[j+1:]="|o"{
            if j == 0 && result[0] != 14 {
                if music_string[j+1:] == "o|" {
                    result[0] = 8
                } else {
                    result[0] += 2
                }
                continue;
            }
            var beat count = 1
            for i:=0;i<len(music_string);i++ {
            	if music_string[j+1:]=="o|" || music_string[j+1:]="|o"{
                    if music_string[j+count] == "o|" {
                        beat += 4
                        result[i] = beat // Beat is one or two, according to how the note sounds.
                        break
                    } else{
                    	beat -= 1 // Beat here should always be equal to 2; and it's just a convenience for us, so we don't have to count each note separately
                    }
                } else {
                    beat = 4 // Beat here should always be equal to 4 - one or two, according to how the note sounds.
                }
           