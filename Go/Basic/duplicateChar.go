package basic

import (
	"fmt"
)

func DuplicateChar() {
	str1 := "abcdeaabcd"
	count1 := make(map[string]int)

	for i := 0; i < len(str1); i++ {
		if count1[string(str1[i])] == 0 {
			count1[string(str1[i])] = 1
		}else {
			count1[string(str1[i])]++
		}
	}

	fmt.Println("The duplicate characters in the string are:")
	fmt.Println(count1)
}