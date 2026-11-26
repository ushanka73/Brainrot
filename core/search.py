import heapq
from core.maze import bisa_dilewati

ARAH =[(-1,0),(1,0),(0,-1),(0,1)]

def heuristic(A,B):
    r1, c1 = A
    r2, c2 = B
    return abs(r1 - r2) +  abs(c1 - c2)    



def tetangga(peta, pos):
    r, c = pos
    hasil = []
    for dr, dc in ARAH :
        nr = r + dr
        nc = c + dc
        if bisa_dilewati(peta, nr, nc):
            hasil.append((nr, nc))
    return hasil



def BestFS(peta, start, goal):
    antrian = []
    heapq.heappush(antrian,(heuristic(start, goal), start))
    asal = {start: None}

    while antrian:
        t, sekarang = heapq.heappop(antrian)

        if sekarang == goal:
            break

        for t in tetangga(peta,sekarang):
            if t not in asal:
                asal[t] = sekarang
                heapq.heappush(antrian,(heuristic(t, goal), t))
    if goal not in asal:
        return []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    jalur = []
    sel = goal
    while sel is not None:
        jalur.append(sel)
        sel = asal[sel]
    jalur.reverse ()
    return jalur

def target_bayang(peta, pos_dava, arah_terakhir):
    dr, dc = arah_terakhir
    target = pos_dava
    for x in range(3):
        r, c = target
        nr, nc = r + dr, c + dc
        if not bisa_dilewati(peta, nr, nc):
            break
        target = (nr, nc)
    return target