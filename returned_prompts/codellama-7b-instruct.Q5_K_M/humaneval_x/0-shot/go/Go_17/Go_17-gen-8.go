
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

	var beats []int
	for _, ch := range music_string {
		switch ch {
		case 'o':
			beats = append(beats, 4)
		case 'o|':
			beats = append(beats, 2)
		case '.|':
			beats = append(beats, 1)
		}
	}
	return beats
}

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

	var beats []int
	for _, ch := range music_string {
		switch ch {
		case 'o':
			beats = append(beats, 4)
		case 'o|':