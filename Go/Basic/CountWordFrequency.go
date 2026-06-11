package basic

import (
	"fmt"
	"strings"
)

func CountWordFrequency(){
	str1 := "hello world hello"
	wordCount := make(map[string]int)

	for _, word := range strings.Fields(str1) {
		wordCount[word]++
	}
	fmt.Println("Word Frequency:")
	for word, count := range wordCount {
		fmt.Printf("%s: %d\n", word, count)
	}
}