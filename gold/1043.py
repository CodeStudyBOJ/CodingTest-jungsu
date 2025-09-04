import copy
def get_known_set(input_str):
    split_input = list(input_str.split())
    if split_input[0] == '0':
        return set()
    return set(map(int, split_input[1:]))

def get_coming_list(input_str):
    split_input = list(map(int, input_str.split()))
    return split_input[1:]

def can_lie(coming_list, known_set):
    for val in coming_list:
        if val in known_set:
            return False
    return True

def find_head_visitor(visit_same_party, target):
    if visit_same_party[target] <= 0:
        return target
    head_visitor = find_head_visitor(visit_same_party, visit_same_party[target])
    visit_same_party[target] = head_visitor
    return head_visitor

def check_visitors(visitors, visit_same_party):
    if len(visitors) == 1:
        return
    
    other_party_visitors = []
    for visitor in visitors:
        if visit_same_party[visitor] != 0:
            other_party_visitors.append(visitor)    
    
    num_other_party_visitor = len(other_party_visitors)
    # 아무도 다른 파티에 참여하지 않음
    if num_other_party_visitor == 0:
        head_visitor = visitors.pop()
        visit_same_party[head_visitor] = -1
        for visitor in visitors:
            visit_same_party[visitor] = head_visitor
    # 한명만 다른 파티에 참여
    elif num_other_party_visitor == 1:
        head_other_party = find_head_visitor(visit_same_party, other_party_visitors[0])
        for visitor in visitors:
            if head_other_party == visitor:
                continue
            visit_same_party[visitor] = head_other_party
    # 여러명이 다른 파티에 참여
    else:
        heads_other_party = set()
        for other_party_visitor in other_party_visitors:
            heads_other_party.add(find_head_visitor(visit_same_party, other_party_visitor))

        head_other_party = heads_other_party.pop()

        for visitor in heads_other_party:
            visit_same_party[visitor] = head_other_party

        for visitor in visitors:
            if head_other_party == visitor:
                continue
            visit_same_party[visitor] = head_other_party

def find_heads_party_visitor(visit_same_party):
    heads_party_visitor = []
    for idx, val in enumerate(visit_same_party):
        if val < 0:
            heads_party_visitor.append(idx)
    return heads_party_visitor

def solution():
    N, M = map(int, input().split())

    first_known_set = get_known_set(input())

    parties = [get_coming_list(input()) for _ in range(M)]

    visit_same_party = [0] * (N+1)
    # 1. 한번이라도 같은 파티에 참여한 사람을 모두 묶기(union-set)
    for party in parties:
        check_visitors(copy.deepcopy(party), visit_same_party)

    # 2. 그 파티에 진실을 아는 사람이 있으면 전부 체크
    heads_party_visitor = find_heads_party_visitor(visit_same_party)

    visitor_hash = {}
    for head_party_visitor in heads_party_visitor:
        visitor_hash[head_party_visitor] = set([head_party_visitor])

    for visitor in range(1,N+1):
        if visit_same_party[visitor] > 0:
            head_visitor = find_head_visitor(visit_same_party, visitor)
            visitor_hash[head_visitor].add(visitor)

    known_set = set()
    
    for known in first_known_set:
        known_set.add(known)
        if visit_same_party[known] == 0:
            continue  
        head_visitor = find_head_visitor(visit_same_party, known)
        if head_visitor in heads_party_visitor:
            for visitor in visitor_hash[head_visitor]:
                known_set.add(visitor)
    
    # # 3. 이후 파티 별로 다시 조사
    ans = 0
    for party in parties:
        if can_lie(party, known_set):
            ans += 1
    print(ans)

solution()
