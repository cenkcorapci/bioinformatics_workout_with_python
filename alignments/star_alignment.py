import align

with open("input.txt") as f:
    content = f.readlines()
    align.match_award, align.mismatch_penalty, align.gap_penalty = [int(x) for x in content[0].split(" ")]
    sequences = []
    for i in xrange(1, len(content)):
        sequences.append(content[i])
    print "Aligning ", len(sequences), " sequences"

