a = "abcdeafabd"

b = a.split("")

done = []
b.forEach(element => {
    if (!done.includes(element)) {
        occ = b.filter((e) => e == element).length
        console.log(element,"  ",occ)
        done.push(element)
    }
});