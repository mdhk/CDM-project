import numpy as np
import nltk
from nltk.util import ngrams
from itertools import chain

from tools.functions import turns

## Complexity measures

def dlg_mul(dlg_sents):
    """
    Mean number of words in utterances.
    """
    # TODO ignore words that are repetitions from previous utterance
    
    # compute utterance length for all utterances
    utt_mul = [[spkID, len(sent)] for spkID, sent in dlg_sents]
    
    # combine utterances into turns
    turn_mul = turns(utt_mul)
        
    # return mean over utterances in turn
    return [[spkID, np.mean(muls)] for spkID, muls in turn_mul]

def dlg_mwl(dlg_sents):
    """
    Mean length of words in utterances.
    """
    # TODO ignore words that are repetitions from previous utterance
    utt_mwl = [[spkID, np.mean([len(w) for w in sent])] 
               if len(sent) > 0 else [spkID, np.nan]
               for spkID, sent in dlg_sents]

    # combine utterances into turns
    turn_mwl = turns(utt_mwl)
    
    return [[spkID, np.mean(mwls)] for spkID, mwls in turn_mwl]

## Alignment measures

def shared_ngrams(turn_i, turn_j, n=1):
    """
    Normalized number of shared ngrams between two turns.
    (unigrams for n = 1, bigrams for n = 2, trigrams for n = 3)
    Use with lexemes for Lexical convergence and with POS
    tags for Syntactic convergence.
    """
    turn_i_ngrams = list(chain.from_iterable([list(ngrams(turn_i[1][i], n)) 
                                         for i in range(len(turn_i[1]))]))
    turn_j_ngrams = list(chain.from_iterable([list(ngrams(turn_j[1][i], n))
                                         for i in range(len(turn_j[1]))]))
    
    # longest turn length (for normalization)
    turnp = [turn_i_ngrams, turn_j_ngrams]
    turn_lengths = [len(turn_i_ngrams), len(turn_j_ngrams)]
    L_i = np.argmax(turn_lengths)
    longer_turn = turnp[L_i]
    shorter_turn = turnp[np.abs(L_i-1)]
    L = len(longer_turn)
    
    if L == 0:
        return np.nan
    
    # amount of ngrams in the longer turn that also occur
    # in the shorter turn
    overlap = len([ngr for ngr in longer_turn if ngr in shorter_turn])
    
    # normalized count
    return overlap / L

## Matrices of differences (in complexity) and convergence (between turns)

# For alignment measures, the alignment / convergence between turns (e.g
# shared lexical or POS tag ngrams) is plotted in the recurrence matrix.

# For complexity measures, the difference in complexity between turns is
# plotted in the recurrence matrix (child's turn - mother's turn).

def diff_matrix(turn_pairs):
    """
    This computes the differences in any given measure between 
    turn i (ADT) and turn j (CHI), and puts them in a matrix.
    """
    n = len(turn_pairs)
            
    # child
    m_turns_j = np.repeat(np.array(turn_pairs)[:,1,1].astype(float), n)
    # adult
    m_turns_i = np.tile(np.array(turn_pairs)[:,0,1].astype(float), n)
    # differences
    diff_vec = m_turns_j - m_turns_i
    
    # adult should be on x-axis of this matrix, child on y-axis
    diff_mat = diff_vec.reshape(n,n)
            
    return diff_mat

def conv_matrix(turn_pairs, n):
    """
    This computes the convergences (shared ngrams) between
    turn i (ADT) and turn j (CHI), and puts them in a matrix.
    
    Can be used with lexemes for lexical convergence or with
    POS tags for syntactic convergence.
    """
    
    N_pairs = len(turn_pairs)
    
    turns_j = [t[1] for t in turn_pairs]
    j_idx = np.repeat(np.arange(N_pairs), N_pairs)
    turns_i = [t[0] for t in turn_pairs]
    i_idx = np.tile(np.arange(N_pairs), N_pairs)
    
    m_vec = np.array([shared_ngrams(turns_i[i], turns_j[j], n=n)
                      for j, i in zip(j_idx, i_idx)])
    
    m_mat = m_vec.reshape(N_pairs,N_pairs)
    
    return m_mat

## Local and global RR

def global_rate(matrix):
    return np.nanmean(matrix)

def local_rate(matrix, d, subset=None):
    """
    This should be RR_d
    """
    # we go over the diagonal of the matrix
    # i.e. consider all points (i, j) where i == j
    # and then we also take the points that are
    # d steps away (above or below) from the diagonal,
    # i.e. from (j, i-d) to (j, i+d)
    # over all those points, we take the mean
    
    # i is i-th turn by participant on the x-axis (adult)
    # j is j-th turn by participant on the y-axis (child)
    
    n = len(matrix)
    
    D = []
    
    # iterate over the diagonal
    for i, j in zip(range(n), range(n)):
        
        # only consider points where j > i
        if subset == 'pos':
            if i < d:
                D.extend(matrix[j, :i])
            else:
                D.extend(matrix[j, i-d:i])
            
        # only consider points where i > j
        elif subset == 'neg':
            if i < d:
                D.extend(matrix[j, i+1:i+1+d])
            else:
                D.extend(matrix[j, i+1:i+1+d])
            
        # consider points in both directions
        else:
            if i < d:
                D.extend(matrix[j, :i+d+1])
            else:
                D.extend(matrix[j, i-d:i+d+1])
                
    return np.nanmean(D)