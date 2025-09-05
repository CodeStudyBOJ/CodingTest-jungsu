class DUS:
    def __init__(self, N):
        self.parent = list(range(N+1))
        self.size = [1] * (N+1)

    def union(self, a, b) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

    def find(self, target) -> int:
        if self.parent[target] != target:
            self.parent[target] = self.find(self.parent[target])
        return self.parent[target]

def solution():
    N, M = map(int, input().split())
    
    tmp = list(map(int, input().split()))
    know = set(tmp[1:]) if tmp[0] > 0 else set()

    parties = []
    
    for _ in range(M):
        line = list(map(int, input().split()))
        _, people = line[0], line[1:]
        parties.append(people)

    dus = DUS(N)

    for people in parties:
        base = people[0]
        for person in people[1:]:
            dus.union(base, person)
        
    know_root = set()
    
    for person in know:
        know_root.add(dus.find(person))
    
    ans = 0

    for people in parties:
        can_lie = True
        for person in people:
            if dus.find(person) in know_root:
                can_lie = False
                break
        if can_lie :
            ans += 1
    
    print(ans)

solution()
