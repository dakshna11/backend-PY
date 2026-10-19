nums=[1,2,3,4,5,6]

squares=[n**2 for n in nums]
evens=[n for n in nums if n%2==0]
lookup={n:n**2 for n in nums} #dict comprehension
unique_lengths={len(w) for w in ["hi", "hey", "ho"]} #set comprehension

print(squares)
print(evens)
print(lookup)
print(unique_lengths)

fruits=["apple", "banana", "cherry"]
fruit_lengths={fruit:len(fruit) for fruit in fruits}
print(fruit_lengths)

num_divisible_by_3_and_5=[n for n in range(1, 50) if n%3==0 and n%5==0]
print(num_divisible_by_3_and_5)

arr=[[1,2,3],[4,5,6],[7,8]]
arr_flattened=[n for sublist in arr for n in sublist]
print(arr_flattened)
