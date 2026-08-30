import heapq

# Define the given graph as an adjacency list with link costs c(u,v)
graph = {
    0: {1: 1, 2: 3, 3: 7},
    1: {0: 1, 2: 1},
    2: {0: 3, 1: 1, 3: 2},
    3: {0: 7, 2: 2}
}

def dijkstra_routing(graph, source):
     # Initialize distances D(v) and predecessors p(v)
     distances = {node: float('infinity') for node in graph}
     distances[source] = 0
     previous_nodes = {node: None for node in graph}
     
     # Priority queue to hold (distance, node)
     pq = [(0, source)]
     
     while pq:
          current_distance, current_node = heapq.heappop(pq)
          
          if current_distance > distances[current_node]:
               continue
               
          for neighbor, weight in graph[current_node].items():
               distance = current_distance + weight
               
               # If a strictly shorter path is found, update it.
               # (Note: Ties are broken implicitly by the order of processing, 
               if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
                    
     return distances, previous_nodes

def get_next_hop(source, destination, previous_nodes):
     """Backtracks from the destination to find the immediate next hop from the source."""
     if previous_nodes[destination] is None:
          return None
     
     current = destination
     while previous_nodes[current] != source:
          current = previous_nodes[current]
     return current


nodes = sorted(graph.keys())

print("=== Link-State Routing Tables ===\n")
for source_node in nodes:
     distances, previous = dijkstra_routing(graph, source_node)
     
     print(f"Routing Table for Node {source_node}:")
     print(f"{'Destination':<15} | {'Next Hop':<10} | {'Total Cost':<10}")
     print("-" * 42)
     
     for dest_node in nodes:
          if dest_node == source_node:
               continue
          next_hop = get_next_hop(source_node, dest_node, previous)
          cost = distances[dest_node]
          print(f"{dest_node:<15} | {next_hop:<10} | {cost:<10}")
     print("\n")