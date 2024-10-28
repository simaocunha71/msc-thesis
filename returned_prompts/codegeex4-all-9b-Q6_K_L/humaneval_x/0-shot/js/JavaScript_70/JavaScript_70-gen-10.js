const strangeSortList = (lst) => {
    if(lst.length === 0) return lst
    let res = []
    let isMin = true
    let arr = [...lst]
    while(arr.length > 0){
        if(isMin){
            res.push(Math.min(...arr))
        }else{
            res.push(Math.max(...arr))
        }
        arr.splice(arr.indexOf(isMin ? Math.min(...arr) : Math.max(...arr)), 1)
        isMin = !isMin
    }
    return res
}