num = [1,2,1,3,4,4,5,3,2,8,6,6]

const dupNum = (num) =>{
    dup = {}
    
    num.forEach((element) => {
        if (element in dup) {
            dup[element] += 1
        }else {
            dup[element] = 1
        }
    });

    return dup 
}

a = dupNum(num)

dupaa = []
Object.keys(a).forEach((e) => {
    if (a[e] > 1) {
        dupaa.push(e)
    }
})

console.log(dupaa)