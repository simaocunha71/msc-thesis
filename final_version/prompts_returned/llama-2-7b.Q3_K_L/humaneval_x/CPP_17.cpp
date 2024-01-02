/*
Input to this function is a string representing musical notes in a special ASCII format.
Your task is to parse this string and return vector of integers corresponding to how many beats does each
not last.

Here is a legend:
"o" - whole note, lasts four beats
"o|" - half note, lasts two beats
".|" - quater note, lasts one beat

>>> parse_music("o o| .| o| o| .| .| .| .| o o")
{4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> parse_music(string music_string){ 
	//code here
	if (music_string == "") return;

	char ch = music_string[0];
	while (ch != '\n') {
		bool o = false, hn = false, qn = false;
		int last_beat = 1; // to check for o in next iteration
		for(int i=1; i<music_string.size(); i++) {
			if (music_string[i] == 'o') o = true, hn = false, qn = false;
			else if (music_string[i] == '|' && last_beat == 1) //checking for whole note
				hn = true, qn = false;
			else if (music_string[i] == '.' && hn == true) { //checking for half note
				qn = true, o=false;
			} else { //checking for quarter note
				qn = false;
				if (o==true && last_beat == 1){
					hn = false;
				}
				last_beat++;
			}

		}//iterating for all the chars of the string except ':'
		if(ch != '\n')