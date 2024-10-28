    vector<int> beat_durations;
    int beat_count = 0;
    for(char c : music_string){
        switch(c){
            case 'o':
                beat_count += 4;
                break;
            case 'o':
                beat_count += 2;
                break;
            case '.':
                beat_count += 1;
                break;
        }
    }
    beat_durations.push_back(beat_count);
    return beat_durations;
}
int main(){
    vector<int> beat_durations = parse_music("o o| .| o| o| .| .| .| .| o o");
    for(int beat_duration : beat_durations){
        printf("%d ", beat_duration);
    }
    printf("\n");
}
