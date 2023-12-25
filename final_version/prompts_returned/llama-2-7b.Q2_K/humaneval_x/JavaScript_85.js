/*Given a non-empty list of integers lst. add the even elements that are at odd indices..


  Examples:
      add([4, 2, 6, 7]) ==> 2 
  */
const add = (lst) => {
    let ret;
    if(lst && lst[0] === null){
        return null;
    }else{
        console.log("check");
        console.log(lst);
        
      for(let i=1;i<lst.length-1;i++){//-1 to get back the first element
            if(lst[i]%2===0)
            ret+=lst[i];
            else{
                const res = lst[i];
                console.log(`res is ${res}`);
                i--;//get back the even index elements for add
                return ret;
            }
        }
    }
}
console.log(add([4, 2, 6, 7]));   // should be 2