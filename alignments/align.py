import sys, string


# test with;
# ACACACTA AGCACACA
# or
# GACTGCAGGGACTCCGACGTTAAGTACATT ACCCTGTCATAGGCGGCGTTCAGGATCACG


# zeros() was origianlly from NumPy.
# This version is implemented by alevchuk 2011-04-10
def zeros(shape):
    retval = []
    for x in range(shape[0]):
        retval.append([])
        for y in range(shape[1]):
            retval[-1].append(0)
    return retval


match_award = 10
mismatch_penalty = -5
gap_penalty = -5  # both for opening and extanding


def match_score(alpha, beta):
    if alpha == beta:
        return match_award
    elif alpha == '-' or beta == '-':
        return gap_penalty
    else:
        return mismatch_penalty


def finalize(align1, align2):
    align1 = align1[::-1]  # reverse sequence 1
    align2 = align2[::-1]  # reverse sequence 2

    i, j = 0, 0

    # calcuate identity, score and aligned sequeces
    symbol = ''
    found = 0
    score = 0
    identity = 0
    for i in range(0, len(align1)):
        # if two AAs are the same, then output the letter
        if align1[i] == align2[i]:
            symbol = symbol + align1[i]
            identity = identity + 1
            score += match_score(align1[i], align2[i])

        # if they are not identical and none of them is gap
        elif align1[i] != align2[i] and align1[i] != '-' and align2[i] != '-':
            score += match_score(align1[i], align2[i])
            symbol += ' '
            found = 0

        # if one of them is a gap, output a space
        elif align1[i] == '-' or align2[i] == '-':
            symbol += ' '
            score += gap_penalty

    identity = float(identity) / len(align1) * 100

    result= Alignment(identity=identity, score=score, seq1=align1, seq2=align2, symbol=symbol)
    result.print_results()
    return result

class Alignment:
    def __init__(self, identity=0.0, score=0.0, seq1="", seq2="", symbol=""):
        self.match_score = score
        self.seq1 = seq1
        self.seq2 = seq2
        self.identity = identity
        self.symbol = symbol

    def print_results(self):
        print 'Identity =', "%3.3f" % self.identity, 'percent'
        print 'Score =', self.match_score
        print self.seq1
        print self.symbol
        print self.seq2
