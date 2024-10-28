    const vowels = "aeiouAEIOU";
    let prev = "";
    let closest = "";
    let closestDist = Infinity;

    for (let char of word) {
        if (vowels.includes(char)) {
            let dist = Math.abs(prev.length - char.length);
            if (dist < closestDist) {
                closestDist = dist;
                closest = char;
            }
            prev = char;
        }
    }

    return closest;
};

/*
  You are given a word. Your task is to find the closest vowel that stands between 
  two consonants from the right side of the word (case sensitive).
  
  Vowels in the beginning and ending doesn't count. Return empty string if you didn't
  find any vowel met the above condition. 

  You may assume that the given string contains English letter only.

  Example:
  getClosestVowel("yogurt") ==> "u"
  getClosestVowel("FULL") ==> "U"
  getClosestVowel("quick") ==> ""
  getClosestVowel("ab") ==> ""
  */






























































































































































































































