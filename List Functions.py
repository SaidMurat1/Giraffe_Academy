lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby", "Oscar"]
print(friends)
# friends.extend(lucky_numbers)
# friends.append(lucky_numbers)
# friends.append("Creed")
# friends.insert(1, "Kelly")
# friends.remove("Jim")
print("index Oscar: ", friends.index("Oscar"))
# Where is "Oscar" / if there is more than one where is the first one
print("count Toby: ", friends.count("Toby"))
# How many "Tobby"s in the list
print("sorted : ", sorted(friends))
print("friends normal: ", friends)
friends.sort()
# sort the list alphabetically
# can not sort a list which contains numbers and strings
print("friends.sort: ", friends)
# friends.reverse():            reverse the list
# friends.sort(reverse=True):   sort in reverse
# copied_friends = friends.copy(): copy friends
# diff between using "=" operator and using "copy" function is when you modify the original list copied list wont effect
# however when you assign and modify, assigned list will be effected
