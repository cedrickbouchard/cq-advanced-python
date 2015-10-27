import numpy as np
# import Pool class


def editDistance(seqA, seqB):
    # Sequence A is vertical (k < M)
    # Sequence B is horizontal (l < N)
    M = len(seqA)
    N = len(seqB)

    allAs = np.tile(np.array(list(seqA)), (N, 1)).T
    allBs = np.tile(np.array(list(seqB)), (M, 1))
    diffs = (allAs != allBs)

    # Dynamic algorithm
    mat = np.tile(0, (M + 1, N + 1))
    mat[:,0] = np.arange(M + 1)
    mat[0,:] = np.arange(N + 1)

    for k in xrange(0, M):
        for l in xrange(0, N):
            mat[k + 1, l + 1] = min(
                mat[k    , l    ] + (1 if diffs[k, l] else 0),
                mat[k    , l + 1] + 1,
                mat[k + 1, l    ] + 1)

    return 'Edit_Distance(%s, %s) = %s'%(seqA, seqB, mat[-1,-1])


def edProxy(twoSeq):
    return editDistance(twoSeq[0], twoSeq[1])


def printRes(results):
    for result in results:
        print(result)


def main():
    sequences = ['attctg,accagt',
                 'ccat,agcattacg',
                 'tacagg,cctgac',
                 'gttcatgga,tccg',
                 'catgcg,gagtac',
                 'tcac,tgcatgcgg']
    distances = []

    for seqs in sequences:
        twoSeq = seqs.split(',', 1)
        distances.append(edProxy(twoSeq))

    # Use edProxy for an easy asynchronous map call
    # Use printRes as a callback function
    printRes(distances)


if __name__ == '__main__':
    main()
