import align


def needle(seq1, seq2):
    m, n = len(seq1), len(seq2)  # length of two sequences

    # Generate DP table and traceback path pointer matrix
    score = align.zeros((m + 1, n + 1))  # the DP table

    # Calculate DP table
    for i in range(0, m + 1):
        score[i][0] = align.gap_penalty * i
    for j in range(0, n + 1):
        score[0][j] = align.gap_penalty * j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = score[i - 1][j - 1] + align.match_score(seq1[i - 1], seq2[j - 1])
            delete = score[i - 1][j] + align.gap_penalty
            insert = score[i][j - 1] + align.gap_penalty
            score[i][j] = max(match, delete, insert)

    # Traceback and compute the alignment
    align1, align2 = '', ''
    i, j = m, n  # start from the bottom right cell
    while i > 0 and j > 0:  # end touching the top or the left edge
        score_current = score[i][j]
        score_diagonal = score[i - 1][j - 1]
        score_up = score[i][j - 1]
        score_left = score[i - 1][j]

        if score_current == score_diagonal + align.match_score(seq1[i - 1], seq2[j - 1]):
            align1 += seq1[i - 1]
            align2 += seq2[j - 1]
            i -= 1
            j -= 1
        elif score_current == score_left + align.gap_penalty:
            align1 += seq1[i - 1]
            align2 += '-'
            i -= 1
        elif score_current == score_up + align.gap_penalty:
            align1 += '-'
            align2 += seq2[j - 1]
            j -= 1

    # Finish tracing up to the top left cell
    while i > 0:
        align1 += seq1[i - 1]
        align2 += '-'
        i -= 1
    while j > 0:
        align1 += '-'
        align2 += seq2[j - 1]
        j -= 1

    align.finalize(align1, align2)


# test------------------------------------------------
seq1, seq2 = raw_input().split(" ")
needle(seq1,seq2)
