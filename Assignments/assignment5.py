
def find_president(S):
    S.sort()                                        # sort the sequence O(NlogN)
    president = S[0]                                # initialize the president with the first id in the sequence
    president_votes = 1
    votes = 1
    for i in range(1, len(S)):                      # loop from i = 1 to N-1
        if S[i] == S[i-1]:                          # if adjacent elements are same
            votes += 1                              # increment votes
        if S[i] != S[i-1] or i == len(S)-1:         # if adjacent elements are different or i = N-1
            if president_votes < votes:             # update the president if votes > president_votes
                president_votes = votes
                president = S[i-1]
            votes = 1                               # reset votes to 1
    return president


S = [10, 874, 10, 874, 92, 384, 92, 874]
print(S)
print(find_president(S))
