
import statistics

data = [3,4,9,11,15,21,22,33,36,48,55]

a = statistics.mean(data)
print(a)

b = statistics.median(data)
print(b)

c = statistics.mode(data)
print(c)

list_1 = [20,40,60,80,100]
list_2 = [30,70,90]

print('Low median of list_1 is :',statistics.median(list_1))
print('Low median of list_2 is :',statistics.median(list_2))

grades = [70,90,50,85,65,83,94]
grades_mean = statistics.mean(grades)
print('Varint of data is :',statistics.variance(grades,grades_mean))


stdevgrades = statistics.stdev(grades)
print('The Standard devation of the list is:',stdevgrades)