num = 20  # You can change this to any number
result = []

for i in range(1, num + 1):
    if num % i == 0:
        result.append(i)

print(result)

# Time Complexity: O(n)
# Space Complexity: O(K) WOULD THE NUMBER OF FACTORS BE K?
# range(1, num + 1): To check all numbers from 1 to num.

# if num % i == 0: Checks if i is a factor of num.

# result.append(i): Adds the factor to the result list