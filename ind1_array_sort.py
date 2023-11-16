# array1 = [2,3,6,7,3,9,12,10]

# # Given an array of integers, arr, find out 2 indices m, n(0<=m<=arr.length-1, 0<=n<=arr.length-1, m<=n), so that as long as all elements in the subarray(from index m to n, indices m and n inclusive) are sorted properly, with this sorted subarray replacing the original subarray, the whole array is sorted (no matter ascendingly or descendingly).
# # The subarray should include the least number of elements required to sort the array completely; means (n-m) must be of the smallest value, and n should also be the smallest one.
# # The function accepts an array of integers (arr) and returns the subarray's start and end index in array format, [m,n] as the result.
# # For example, in an array [1,2,3,6,4,4], the SMALLEST subarray (least numbers of integers) to be sorted is [6,4,4], if we sort it to [4,4,6], then replace the original subarray, the whole array now turns to be[1,2,3,4,4,6], which is sorted completely. This subarray begins from index 3, and ends in index 5, so the result is [3,5].
# # If all elements in the array are the same, return array [0,0]. 
# # If all elements in the array are already sorted, no matter ascendingly or descendingly, return [0,0] as well.



# def solution(arr):
#     result = arr.sort
#     pass





# test1 = solution(array1)