let map = {}

lst.forEach(num => {
    if(map[num]){
        map[num]++
    } else {
        map[num] = 1
    }
})

let max = -1
let min = Infinity

for(let i = 0; i< lst.length; i++){
    if(map[lst[i]] > lst[i]){
        max = Math.max(max, lst[i])
        min = Math.min(min, lst[i])
    }
}

if(max === -1){
    return max
}

for(let i = min; i <= max; i++){
    if(map[i] >= i){
        return i
    }
}

return -1
};

search([4, 1, 2, 2, 3, 1]) // 2
search([1, 2, 2, 3, 3, 3, 4, 4, 4]) // 3
search([5, 5, 4, 4, 4]) // -1


*/


















































































































































































































































