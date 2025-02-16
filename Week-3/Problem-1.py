def longest_subarray_with_sum_k(arr, k):
    prefix_sums = {}
    current_sum = 0
    max_length = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum == k:
            max_length = i + 1

        if current_sum not in prefix_sums:
            prefix_sums[current_sum] = i

    return max_length

arr=[10, -10, 20, 30]
k=-5
longest_subarray_with_sum_k(arr,k)