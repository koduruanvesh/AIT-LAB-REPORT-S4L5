
graph = {
    'a': {'b': 2,'d':4},
    'b': {'c': 3},
    'c': {'d': 1},
    'd': {'a': 4}
}

visited=set()
def gr(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            gr(visited,graph,neighbour)
print('graph nodes are:')
gr(visited,graph,'a')
cost_ab = graph['a']['b']
cost_bc = graph['b']['c']
cost_cd = graph['c']['d']
cost_da = graph['d']['a']

print(f"Cost from a to b: {cost_ab}")
print(f"Cost from b to c: {cost_bc}")
print(f"Cost from c to d: {cost_cd}")
print(f"Cost from d to a: {cost_da}")
total_cost = cost_ab + cost_bc + cost_cd + cost_da
print(f"Total cost: {total_cost}")


