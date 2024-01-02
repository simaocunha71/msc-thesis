/*Given a string representing a space separated lowercase letters, return a dictionary
  of the letter with the most repetition and containing the corresponding count.
  If several letters have the same occurrence, return all of them.
  
  Example:
  histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
  histogram('a b b a') == {'a': 2, 'b': 2}
  histogram('a b c a b') == {'a': 2, 'b': 2}
  histogram('b b b b a') == {'b': 4}
  histogram('') == {}

  */
const histogram = (test) => {
    let newString = test.split(" ").join(``)`;
    let result = {};
    for (let character of newString){
        if(!result[character]){
            result[character] = 1;
        }else{
            result[character]++;
        }
        
    }
    console.log("Histogram: ");
    return result;
}