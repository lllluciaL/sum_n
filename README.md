# sum_n
Functional Requirements:
(1) Data import: Enter an integer array and the n value of the sum of n numbers you want to get.
(2) Data processing: Reorder the array in ascending order.
(3) Data analysis: Use two pointers to traverse the data, find n-tuples that meet the task requirements, and perform deduplication operations on the tuples.
Data output: Output all tuples that meet the conditions

Technical route
(1) sort() function, which is used to sort the input array in ascending order to facilitate later calculations.
(2) fourSum_enumeration() function, this function is used to find the array of 4 elements in the array that satisfies the sum value of t in an enumeration manner.
(3) fourSum_pointer() function, this function is used to find the array of 4 elements in the array that satisfies the sum value of t in the form of double pointers.
(4) nSum() function, which is used to find an array of n elements in the array that satisfies the sum value of t in a depth-first search manner.
(5) fourSum() function, this function uses the backtracking method to deeply search the array and classify the data. Elements that meet the conditions are added to the four-tuple, elements that do not meet the conditions are added to the notSelected list, and the value will not be added later. function, reducing search complexity and data volume.
(6) main() function, use the time() function to calculate the running time of the above three calculation functions, and finally compare them.
