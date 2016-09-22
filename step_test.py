
def split_seq(n):
    print("Value: %d" %n)
    count = 0
    if n>2:
        range_val = (n/2)
        for idx in xrange(n-1,range_val-1,-1):
            i = idx
            j = n-idx
            if j<i:
                count = count + 1
                print([idx,n-idx])

    return count

if __name__ == "__main__":
    ref = 3
    for n in xrange(1,10):
    #cut_number_refs(ref,n)
        print("Total partitions: %d " %split_seq(n))
