import align

def water(seq1, seq2):
    m, n = len(seq1), len(seq2)  # length of two sequences

    # Generate DP table and traceback path pointer matrix
    score = align.zeros((m + 1, n + 1))  # the DP table
    pointer = align.zeros((m + 1, n + 1))  # to store the traceback path
    max_i, max_j = 0, 0
    max_score = 0  # initial maximum score in DP table
    # Calculate DP table and mark pointers
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            score_diagonal = score[i - 1][j - 1] + align.match_score(seq1[i - 1], seq2[j - 1])
            score_up = score[i][j - 1] + align.gap_penalty
            score_left = score[i - 1][j] + align.gap_penalty
            score[i][j] = max(0, score_left, score_up, score_diagonal)
            if score[i][j] == 0:
                pointer[i][j] = 0  # 0 means end of the path
            if score[i][j] == score_left:
                pointer[i][j] = 1  # 1 means trace up
            if score[i][j] == score_up:
                pointer[i][j] = 2  # 2 means trace left
            if score[i][j] == score_diagonal:
                pointer[i][j] = 3  # 3 means trace diagonal
            if score[i][j] >= max_score:
                max_i = i
                max_j = j
                max_score = score[i][j]

    align1, align2 = '', ''  # initial sequences

    i, j = max_i, max_j  # indices of path starting point

    # traceback, follow pointers
    while pointer[i][j] != 0:
        if pointer[i][j] == 3:
            align1 += seq1[i - 1]
            align2 += seq2[j - 1]
            i -= 1
            j -= 1
        elif pointer[i][j] == 2:
            align1 += '-'
            align2 += seq2[j - 1]
            j -= 1
        elif pointer[i][j] == 1:
            align1 += seq1[i - 1]
            align2 += '-'
            i -= 1

    align.finalize(align1, align2)


#test------------------------------------------------
seq1, seq2 = raw_input().split(" ")
water(seq1,seq2)
