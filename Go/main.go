package main

import "fmt"


func main() {
	num := []int{1,2,1,3,4,4,5,3,2,8,6,6}
	fmt.Println("The duplicate elements in the array are:")
	done := make(map[int]bool)

	for i := 0; i < len(num); i++ {
		if done[num[i]] {
			continue
		}
		for j := i + 1; j < len(num); j++ {
			if num[i] == num[j] {
				fmt.Println(num[i])
				done[num[i]] = true
				break
			}
		}
	}
}