def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i-1
        key = l[i]
        while (l[j] > key) and (j >= 0):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
        print l


unsorted = [10, 3, 23, 9, 234, 454, 12312, 11 ]

insertion_sort(unsorted)
print
print unsorted
