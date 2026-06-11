text = "Js is easy and Js is powerful"

words = text.split(" ");

freq = {}

for (let i = 0; i < words.length; i++) {
    words[i] in freq
        ? freq[words[i]]++
        : freq[words[i]] = 1
}

console.log(freq)