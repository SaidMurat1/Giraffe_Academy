set1 = set([1, 3, 5])
set2 = set([1, 2, 3])
# set1'de olup set2'de olmayanlar.
print(set1.difference(set2))
#
print(set1.intersection(set2))
# symmetric_difference():İki kümede de birbirlerine göre olmayanlar
print(set1.symmetric_difference(set2))