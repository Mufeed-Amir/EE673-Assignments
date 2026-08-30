import copy

# Infinity representation
INF = 999

# Format for the communication packet as defined in the assignment
class rtpkt:
     def __init__(self, sourceid, destid, mincost):
          self.sourceid = sourceid
          self.destid = destid
          self.mincost = copy.deepcopy(mincost)

# Global event queue to emulate the network layer (tolayer2)
packet_queue = []

def tolayer2(packet):
     packet_queue.append(packet)

# --- NODE 0 ROUTINES ---
# dt0[destination][neighbor_used]
dt0 = [[INF]*4 for _ in range(4)]
mincost0 = [INF]*4
neighbors0 = [1, 2, 3]

def rtinit0():
     global dt0, mincost0
     # Initialize direct link costs
     dt0[0][0] = 0
     dt0[1][1] = 1
     dt0[2][2] = 3
     dt0[3][3] = 7
     
     # Set initial mincosts
     mincost0 = [0, 1, 3, 7]
     
     # Notify neighbors
     for n in neighbors0:
          tolayer2(rtpkt(0, n, mincost0))

def rtupdate0(pkt):
     global dt0, mincost0
     sender = pkt.sourceid
     changed = False
     
     # Update the distance table with the neighbor's new vector
     for dest in range(4):
          # Cost to dest via sender = cost to sender + sender's mincost to dest
          new_cost = dt0[sender][sender] + pkt.mincost[dest]
          dt0[dest][sender] = new_cost
          
          # Recalculate minimum cost to this destination
          current_min = min(dt0[dest])
          if current_min < mincost0[dest]:
               mincost0[dest] = current_min
               changed = True
               
     # If our minimum costs changed, we must inform our neighbors
     if changed:
          for n in neighbors0:
               tolayer2(rtpkt(0, n, mincost0))

# --- NODE 1 ROUTINES ---
dt1 = [[INF]*4 for _ in range(4)]
mincost1 = [INF]*4
neighbors1 = [0, 2]

def rtinit1():
     global dt1, mincost1
     dt1[0][0] = 1
     dt1[1][1] = 0
     dt1[2][2] = 1
     dt1[3][3] = INF # No direct link to 3
     mincost1 = [1, 0, 1, INF]
     
     for n in neighbors1:
          tolayer2(rtpkt(1, n, mincost1))

def rtupdate1(pkt):
     global dt1, mincost1
     sender = pkt.sourceid
     changed = False
     for dest in range(4):
          new_cost = dt1[sender][sender] + pkt.mincost[dest]
          dt1[dest][sender] = new_cost
          current_min = min(dt1[dest])
          if current_min < mincost1[dest]:
               mincost1[dest] = current_min
               changed = True
     if changed:
          for n in neighbors1:
               tolayer2(rtpkt(1, n, mincost1))

# --- NODE 2 ROUTINES ---
dt2 = [[INF]*4 for _ in range(4)]
mincost2 = [INF]*4
neighbors2 = [0, 1, 3]

def rtinit2():
     global dt2, mincost2
     dt2[0][0] = 3
     dt2[1][1] = 1
     dt2[2][2] = 0
     dt2[3][3] = 2
     mincost2 = [3, 1, 0, 2]
     
     for n in neighbors2:
          tolayer2(rtpkt(2, n, mincost2))

def rtupdate2(pkt):
     global dt2, mincost2
     sender = pkt.sourceid
     changed = False
     for dest in range(4):
          new_cost = dt2[sender][sender] + pkt.mincost[dest]
          dt2[dest][sender] = new_cost
          current_min = min(dt2[dest])
          if current_min < mincost2[dest]:
               mincost2[dest] = current_min
               changed = True
     if changed:
          for n in neighbors2:
               tolayer2(rtpkt(2, n, mincost2))

# --- NODE 3 ROUTINES ---
dt3 = [[INF]*4 for _ in range(4)]
mincost3 = [INF]*4
neighbors3 = [0, 2]

def rtinit3():
     global dt3, mincost3
     dt3[0][0] = 7
     dt3[1][1] = INF
     dt3[2][2] = 2
     dt3[3][3] = 0
     mincost3 = [7, INF, 2, 0]
     
     for n in neighbors3:
          tolayer2(rtpkt(3, n, mincost3))

def rtupdate3(pkt):
     global dt3, mincost3
     sender = pkt.sourceid
     changed = False
     for dest in range(4):
          new_cost = dt3[sender][sender] + pkt.mincost[dest]
          dt3[dest][sender] = new_cost
          current_min = min(dt3[dest])
          if current_min < mincost3[dest]:
               mincost3[dest] = current_min
               changed = True
     if changed:
          for n in neighbors3:
               tolayer2(rtpkt(3, n, mincost3))

# --- MAIN EMULATION ALGORITHM ---
def main():
     print("--- Starting DV Routing Emulation ---")
     
     # 1. Initialize all nodes
     rtinit0()
     rtinit1()
     rtinit2()
     rtinit3()
     
     # 2. Process packets until the network converges (queue is empty)
     step = 1
     while packet_queue:
          # Pop the oldest packet from the queue
          pkt = packet_queue.pop(0)
          
          # Route the packet to the correct destination node's update routine
          if pkt.destid == 0:
               rtupdate0(pkt)
          elif pkt.destid == 1:
               rtupdate1(pkt)
          elif pkt.destid == 2:
               rtupdate2(pkt)
          elif pkt.destid == 3:
               rtupdate3(pkt)
               
          step += 1
          
     print(f"Network converged after processing {step} updates.")
     print("\n--- Final Minimum Cost Vectors ---")
     print(f"Node 0: {mincost0}")
     print(f"Node 1: {mincost1}")
     print(f"Node 2: {mincost2}")
     print(f"Node 3: {mincost3}")

if __name__ == "__main__":
    main()