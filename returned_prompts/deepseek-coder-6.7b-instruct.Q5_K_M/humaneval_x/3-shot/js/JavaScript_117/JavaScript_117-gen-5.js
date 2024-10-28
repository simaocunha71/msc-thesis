  const vowels 		= 	['a', 'e', 'i', 'o', 'u'];
  let words 			= 	s.split(' ');
  let selectedWords = [];

  for(let i = 0; i < words.length; i++){
  	let consonantCount = 0;
  	for(let j = 0; j < words[i].length; j++){
  		if(!vowels.includes(words[i][j]) && isNaN(words[i][j])){
  			consonantCount++;
  		}
  	}
  	if(consonantCount === n){
  		selectedWords.push(words[i]);
  	}
  }
  return selectedWords;
}



