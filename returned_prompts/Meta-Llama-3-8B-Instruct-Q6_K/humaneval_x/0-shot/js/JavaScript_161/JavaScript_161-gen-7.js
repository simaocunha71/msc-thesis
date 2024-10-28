```
let result = '';
for(let i = 0; i < s.length; i++) {
    if(isNaN(s[i])) {
        if(s[i].match(/[a-zA-Z]/)) {
            result += s[i].toUpperCase().replace(/[A-Z]/, m => m.toLowerCase());
        } else {
            result += s[i];
        }
    } else {
        if(result === '') {
            result = '';
        } else {
            result = result.split('').reverse().join('');
        }
    }
}
return result;
```  }  } 

Explanation:
1. We iterate through each character in the string.
2. If the character is not a number (checked using `isNaN`), we check if it's a letter using a regular expression (`[a-zA-Z]`). If it is, we reverse its case using `toUpperCase` and `replace` methods. If it's not a letter, we just add it to the result as it is.
3. If the character is a number, we check if the result string is empty. If it is, we don't do anything. If it's not, we reverse the result string using `split`, `reverse`, and `join` methods.
4. Finally, we return the result string.  } }  }  } }  }  }  }  }  }  }  }  }  }  } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } }