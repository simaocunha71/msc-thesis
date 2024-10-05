	for(int i=word.size()-1;i>=0;i--){
		if(i!=word.size()-1 && word[i]=='a' || word[i]=='e' || word[i]=='i'|| word[i]=='o'|| word[i]=='u'){
			while(i!=0 && word[i-1]!='a' && word[i-1]!='e' && word[i-1]!='i' && word[i-1]!='o' && word[i-1]!='u'){
				i--;
			}
			while(i!=word.size()-1 && word[i+1]!='a' && word[i+1]!='e' && word[i+1]!='i' && word[i+1]!='o' && word[i+1]!='u'){
				i++;
			}
			if(i!=0 && word[i-1]=='a' && word[i-1]=='e' && word[i-1]=='i' && word[i-1]=='o' && word[i-1]=='u'){
				continue A;
			}
			if(i!=word.size()-1 && word[i+1]=='a' && word[i+1]=='e' && word[i+1]=='i' && word[i+1]=='o' && word[i+1]=='u'){
				continue A;
			}
			return word[i];
		}
	}
	return "";
}

int main(){
	string word;
	while(cin>>word){
		cout<<get_closest_vowel(word)<<endl;
	}
	return 0;
}

*/







































