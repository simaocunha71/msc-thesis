
// let arr = []
// for(let i = 0; i < s.length; i++) {
//     let temp = s[i];
//     for(let j = i + 1; j < s.length; j++) {
//         temp += s[j];
//         arr.push(temp);
//     }
// }

// let check = true;
// while(arr.length > 0) {
//     let temp = arr.length % 3 === 0 ? arr.length : 3;
//     let str = arr.slice(0, temp).join('');
//     if(arr.length === temp) {
//         check = false;
//         break;
//     }
//     if(str.length > 0 && new Set(str).size !== str.length) {
//         check = true;
//         arr = [];
//     } else {
//         check = false;
//         arr = [];
//     }
// }

// return check;

let arr = [];
for(let i = 0; i < s.length; i++) {
    let temp = s[i];
    for(let j = i + 1; j < s.length; j++) {
        temp += s[j];
        arr.push(temp);
    }
}

let check = true;
while(arr.length > 0) {
    let temp = arr.length % 3 === 0 ? arr.length : 3;
    let str = arr.slice(0, temp).join('');
    if(arr.length === temp) {
        check = false;
        break;
    }
    if(str.length > 0 && new Set(str).size === str.length) {
        check = false;
        arr = [];
    } else {
        check = true;
        arr = [];
    }
}

return check;
};


module.exports = { isHappy };

*/








































