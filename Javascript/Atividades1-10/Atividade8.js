let num=[5,8,2,10,3]
let maior= num[0]
for (let i of num){
    if ( i > maior ){
      maior =i
     }
}
console.log(maior)