    let newArr = []
    arr.forEach(item => {
        if(item >= 1 && item <= 9){
            newArr.push(item)
        }
    })
    newArr.sort((a, b) => a - b)
    let newArr2 = []
    for(let i = newArr.length - 1; i >= 0; i--){
        newArr2.push(newArr[i])
    }
    let newArr3 = []
    for(let i = 0; i < newArr2.length; i++){
        switch(newArr2[i]){
            case 1:
                newArr3.push('One')
                break;
            case 2:
                newArr3.push('Two')
                break;
            case 3:
                newArr3.push('Three')
                break;
            case 4:
                newArr3.push('Four')
                break;
            case 5:
                newArr3.push('Five')
                break;
            case 6:
                newArr3.push('Six')
                break;
            case 7:
                newArr3.push('Seven')
                break;
            case 8:
                newArr3.push('Eight')
                break;
            case 9:
                newArr3.push('Nine')
                break;
        }
    }
    return newArr3
}
module.exports = byLength;

*/








































































































































