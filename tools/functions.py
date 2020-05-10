import numpy as np

## Extracting turns from dialogues

# Following follows Fernandez & Grimm (2014): 
# "We consider a turn to be a stretch of speech by one speaker, 
# which may include more than one utterance".

def turns(utt_measures):
    """
    Aggregate per-utterance measures into turns.
    """
    turns = []
    
    # go over every utterance
    for i, (spk, ms) in enumerate(utt_measures):
        
        # check the speaker of the previous turn
        prev_spk = utt_measures[i-1][0] if i > 0 else None
        
        # if the previous utterance had the same
        # speaker as the current utterance, add
        # to the same turn
        if spk == prev_spk:
            turns[-1][1].append(ms)
        else:
            turns.append([spk, [ms]])
    return turns

def turn_pairs(turn_measures):
    """
    This extracts sequential (ADT, CHI) pairs from the dialogue, 
    to compute the recurrence plot measures over.
    
    Note: includes investigator turns!
    """
    turn_pairs = []
    for i, turn in enumerate(turn_measures[:-1]):
        if turn[0] != 'CHI' and turn_measures[i+1][0] == 'CHI':
            turn_pairs.append([turn, turn_measures[i+1]])
    return turn_pairs

## Statistics

def nansem(samples):
    """
    Estimated standard error of the mean
    = (standard deviation / sqrt(sample size)),
    with NaN values ignored.
    """
    return np.nanstd(samples) / np.sqrt(len(samples))