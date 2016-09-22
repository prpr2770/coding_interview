# test for the grandest stairway problem:

def cut_number_refs(ref,n):
    if n>2:
        if  n > ref:
            print("\tn>ref\n")
            for idx in xrange(1,ref+1):
                cut_number_refs(idx,n-idx)
        else:
            print("\tn<=ref")
            print('\t'+ str([ref,n]))
            for idx in xrange(1,n):
                #print('\t'+ str([n-idx,idx]))
                cut_number_refs(n-idx,idx)
    else:
        print("NULL")


# ------------------------------------------------------------------------
# RECURSION:

def numways(n,ref):
    # return the total number of paths available.
    #print("(n,ref) = (%d,%d)"%(n,ref))
    countways = 0
    if n>2:
        if n<= ref: # vanilla case!
            countways = (n-1)/2 #
            for idx in xrange(n-1,0,-1):
                countways = countways + numways(n-idx,idx)
        else:
            for idx in xrange(ref,0,-1):
                countways =  countways + numways(n-idx,idx)
    print('\t (n,ref,ways) = (%d,%d,%d) ' % (n,ref,countways))
    return countways


# ------------------------------------------------------------------------
# MEMOIZE RECURSION:

dict_numways = {1:0, 2:0}


def numways2(n,ref):
    # return the total number of paths available.
    #str_seq = str_seq + "("+ str(n) + ","+ str(ref) + ") -> "
    countways = 0
    if n>2:
        if n<= ref: # vanilla case!
            if n in dict_numways.keys():
                countways = dict_numways[n]
            else: # value NOT present in dictionary
                # compute the ways-count
                countways = (n-1)/2
                for idx in xrange(n-1,0,-1):
                    key = (n-idx)
                    countways = countways + numways2(key,idx)
                #update dictionary with value:
                print("update dict (n,ref) = (%d,%d) with (n= %d, ways = %d)" %(n,ref,n,countways))
                dict_numways[n] = countways
        else: # n > ref
            if n/2 < ref:
                for idx in xrange(ref-1,0,-1):
                        countways =  countways + numways2(n-idx,idx) # works slow.
                    #countways =  countways + numways2(n-idx,ref) # is this correct?
    #print('\t %d' % countways)
    print('\t (n,ref,ways) = (%d,%d,%d) ' % (n,ref,countways))
    return countways



if __name__ == "__main__":

    Nmax = 200
    #for n in xrange(1,Nmax+1):
    #    print(" (n= %d, ways = %d )"% (n, numways(n,n)))

    n = Nmax
    #print("algo1: (n= %d, ways = %d )"% (n, numways(n,n)))

    print("algo2:  (n= %d, ways = %d )"% (n, numways2(n,n)))
    #print(dict_numways)
    #print str_seq
