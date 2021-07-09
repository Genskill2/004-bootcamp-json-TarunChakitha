import json

def load_journal(filename: str):
    with open(filename,'r') as file:
        data = json.load(file)    
    return data

def compute_phi(filename: str, event):
    data = load_journal(filename)
    # phi = 0
    n_1 = n_0 = 0 # Y is true no matter X (Squirrel is True no matter Event)
    n0_ = n1_ = 0 # X is true no matter Y ( ... )

    n00 = 0 # both event and Squirrel are False
    n01 = 0 # Event is False but Squirrel is True
    n10 = 0 # Event is True but Squirrel is False
    n11 = 0 # both Event and Squirrel are True

    for d in data:
        squirrel = d['squirrel']
        event_list = d['events']

        if squirrel: n_1 += 1
        else: n_0 += 1

        if event in event_list:
            n1_ += 1
            if squirrel: n11 += 1
            else: n10 += 1
        else:
            n0_ += 1
            if squirrel: n01 += 1
            else: n00 += 1

    ϕ = (n11 * n00 - n10 * n01) / ((n1_ * n0_ * n_1 * n_0)**(0.5))
    return ϕ
    
def compute_correlations(filename):
    data = load_journal(filename)
    big = []
    for d in data:
        big = big + d['events']
    all_events = dict.fromkeys(big)
    for event in all_events.keys():
        all_events[event] = compute_phi(filename,event)
    return all_events

def diagnose(filename):
    all_events = compute_correlations(filename=filename)
    highly_pos_correlation = list(all_events.keys())[list(all_events.values()).index(max(all_events.values()))]
    highly_neg_correlation = list(all_events.keys())[list(all_events.values()).index(min(all_events.values()))]

    # return ['asf','asfsd']
    return [highly_pos_correlation, highly_neg_correlation]
