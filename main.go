package main

import "fmt"

func next_greatest_element(arr1 []int, arr2 []int) []int {

	next_greatest := make(map[int]int)

	great := -1

	for i := len(arr2) - 1; i >= 0; i-- {
		if great == -1 {
			next_greatest[arr2[i]] = -1
			great = arr2[i]
		} else {
			term := arr2[i]

			if term > great {
				next_greatest[arr2[i]] = -1
			} else {
				next_greatest[arr2[i]] = great
			}

			great = arr2[i]

		}
	}

	ans := []int{}

	for i := 0; i < len(arr1); i++ {
		ans = append(ans, next_greatest[arr1[i]])
	}

	return ans
}

func main() {

	fmt.Println(next_greatest_element([]int{4, 3, 1, 2}, []int{1, 3, 4, 2}))
}
