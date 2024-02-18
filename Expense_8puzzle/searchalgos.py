from collections import deque
from queue import PriorityQueue

class Searchalgo:
    def __init__(self,log):
        self.log = log
        self.tile_costs_dicts = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}

    def findzero(self, state):
        for a in range(3):
                for b in range(3):
                    if(state[a][b] == 0):
                        i,j = a,b
        return i,j

    def man_distance(self,state):
        m = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    m += self.tile_costs_dicts[state[i][j]] * (abs(((state[i][j]-1) // 3) -i) + abs(((state[i][j]-1) % 3)-j))
        return m

    def astar_search(self,initial_state, goal_state):
        store_Queue = []
        store_Queue.append((self.man_distance(initial_state), [initial_state], 0,[]))
        pops = 0
        nodes = 1
        MAx_Q = 1
        explored = set()
        while len(store_Queue) > 0:
            pops +=1
            MAx_Q = max(len(store_Queue),MAx_Q)
            print(store_Queue)
            store_Queue.sort(key = lambda i:i[0])
            a,b,c,d = store_Queue.pop(0)
            self.log.info("%s ----- %s ----- %s ------ %s",str(a),str(b),str(c),str(d))
            h, path, cost, directions = a,b,c,d
            current_state = path[-1]
            if current_state == goal_state:
                print("Nodes Popped : ", pops)
                print('Nodes Expanded : ', len(explored))
                print("Nodes Genarated : ", str(nodes))
                print("Max Fringe size : ", str(MAx_Q))
                print("Solution found at Depth : ", len(directions))
                print("Cost : ",cost)
                print("Directions for Solution: ")
                for i in directions:
                    print(i)
                self.log.info("Nodes Popped : %s", pops)
                self.log.info('Nodes Expanded : %s', len(explored))
                self.log.info("Nodes Genarated : %s", str(nodes))
                self.log.info("Max Fringe size : %s", str(MAx_Q))
                self.log.info("Solution found at Depth : %s", len(directions))
                self.log.info("Cost : %s",cost)
                self.log.info("Directions for solution: %s", directions)
                return path
            if tuple(map(tuple, current_state)) in explored:
                continue
            i,j = self.findzero(current_state)
            gi, gj = i + 0, j - 1
            if 0 <= gi < 3 and 0 <= gj < 3:
                new_state = [row.copy() for row in current_state]
                new_state[i][j] = new_state[gi][gj]
                new_state[gi][gj] = 0
                new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
                nodes += 1
                store_Queue.append((new_cost + self.man_distance(new_state), path + [new_state], new_cost,directions+ ["Right "+str(new_state[i][j])]))
            gi, gj = i + 0, j + 1
            if 0 <= gi < 3 and 0 <= gj < 3:
                new_state = [row.copy() for row in current_state]
                new_state[i][j] = new_state[gi][gj]
                new_state[gi][gj] = 0
                new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
                nodes += 1
                store_Queue.append((new_cost + self.man_distance(new_state), path + [new_state], new_cost,directions + ["Left "+str(new_state[i][j])]))
            gi, gj = i - 1, j + 0
            if 0 <= gi < 3 and 0 <= gj < 3:
                new_state = [row.copy() for row in current_state]
                new_state[i][j] = new_state[gi][gj]
                new_state[gi][gj] = 0
                new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
                nodes += 1
                store_Queue.append((new_cost + self.man_distance(new_state), path + [new_state], new_cost, directions + ["Down "+str(new_state[i][j])]))
            gi, gj = i + 1, j + 0
            if 0 <= gi < 3 and 0 <= gj < 3:
                new_state = [row.copy() for row in current_state]
                new_state[i][j] = new_state[gi][gj]
                new_state[gi][gj] = 0
                new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
                nodes += 1
                store_Queue.append((new_cost + self.man_distance(new_state), path + [new_state], new_cost,directions + ["Up "+str(new_state[i][j])]))
            explored.add(tuple(map(tuple, current_state)))
        return None
    
    def dfs(self,goal_state, state, path, cost, explored, directions):
        nodes =0
        if tuple(map(tuple, state)) == tuple(map(tuple, goal_state)):
            print('Nodes Expanded : ', len(explored))
            print("Nodes Genarated : ", str(nodes))
            print("Solution found at Depth : ", len(directions))
            print("Cost : ",cost)
            print("Directions for Solution: ")
            for i in directions:
                print(i)
            self.log.info('Nodes Expanded : %s', len(explored))
            self.log.info("Node Genarated : %s", str(nodes))
            self.log.info("Solution found at Depth : %s", len(directions))
            self.log.info("Cost : %s",cost)
            self.log.info("Directions: %s", directions)
            return path
        if tuple(map(tuple, state)) in explored:
            return None
        explored.add(tuple(map(tuple, state)))
        i,j = self.findzero(state)

        gi, gj = i + 0, j - 1
        if 0 <= gi < 3 and 0 <= gj < 3:
            nodes+=1
            new_state = [row.copy() for row in state]
            new_state[i][j] = new_state[gi][gj]
            new_state[gi][gj] = 0
            new_path = path + [new_state]
            new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
            new_direction = directions + ["UP"+str(new_state[i][j])]
            result = self.dfs(goal_state,new_state, new_path, new_cost, explored, new_direction)
            if result is not None:
                return result

        gi, gj = i + 0, j + 1
        if 0 <= gi < 3 and 0 <= gj < 3:
            nodes+=1
            new_state = [row.copy() for row in state]
            new_state[i][j] = new_state[gi][gj]
            new_state[gi][gj] = 0
            new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
            new_path = path + [new_state]
            new_direction = directions + ["DOWN"+str(new_state[i][j])]
            result = self.dfs(goal_state,new_state, new_path, new_cost, explored, new_direction)
            if result is not None:
                return result

        gi, gj = i - 1, j + 0
        if 0 <= gi < 3 and 0 <= gj < 3:
            nodes+=1
            new_state = [row.copy() for row in state]
            new_state[i][j] = new_state[gi][gj]
            new_state[gi][gj] = 0
            new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
            new_path = path + [new_state]
            new_direction = directions + ["Left"+str(new_state[i][j])]
            result = self.dfs(goal_state,new_state, new_path, new_cost, explored, new_direction)
            if result is not None:
                return result

        gi, gj = i + 1, j + 0
        if 0 <= gi < 3 and 0 <= gj < 3:
            nodes+=1
            new_state = [row.copy() for row in state]
            new_state[i][j] = new_state[gi][gj]
            new_state[gi][gj] = 0
            new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
            new_path = path + [new_state]
            new_direction = directions + ["Right"+str(new_state[i][j])]
            result = self.dfs(goal_state,new_state, new_path, new_cost, explored, new_direction)
            if result is not None:
                return result
        return None

    def dfs_search(self,initial_state, goal_state):
        return self.dfs(goal_state,initial_state, [initial_state], 0, set(),[])
    
    def bfs_search(self, initial_state, goal_state):
        c = 0
        nodes = 1
        store_place = deque([(initial_state, [initial_state], 0,[])])
        expl = set()
        MAx_Q = 0
        while store_place:
            c+=1
            MAx_Q = max(MAx_Q,len(store_place))
            state, path, cost,directions = store_place.popleft()
            self.log.info("%s ----- %s ----- %s ------ %s",str(state),str(path),str(cost),str(directions))
            if tuple(map(tuple, state)) == tuple(map(tuple, goal_state)):
                print("Nodes popped : ", c)
                print('Nodes Expanded : ', len(expl))
                print("Nodes Genarated : ", str(nodes))
                print("Max Fringe size : ", str(MAx_Q))
                print("Solution found at Depth : ", len(directions))
                print("Cost : ",cost)
                print("Directions for Solution: ")
                for i in directions:
                    print(i)
                self.log.info("Nodes Popped : %s", c)
                self.log.info('Nodes Expanded : %s', len(expl))
                self.log.info("Nodes Genarated : %s", str(nodes))
                self.log.info("Max Fringe size : %s", str(MAx_Q))
                self.log.info("Solution found at Depth : %s", len(directions))
                self.log.info("Cost : %s",cost)
                self.log.info("Directions for Solution: %s", directions)
                return path
            expl.add(tuple(map(tuple, state)))
            i,j = self.findzero(state)
            for ti, tj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                gi, gj = i + ti, j + tj
                if 0 <= gi < 3 and 0 <= gj < 3:
                    nodes +=1 
                    new_state = [row.copy() for row in state]
                    new_state[i][j] = new_state[gi][gj]
                    new_state[gi][gj] = 0
                    new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
                    new_path = path + [new_state]
                    t = ""
                    if((ti,tj) == (0,-1)):
                        t = "UP"
                    elif((ti,tj) == (0,1)):
                        t = "Down"
                    elif((ti,tj) == (-1,0)):
                        t = "Left"
                    elif((ti,tj) == (1,0)):
                        t = "Right"
                    new_direction = directions+[t+" "+str(new_state[i][j])]
                    if tuple(map(tuple, new_state)) not in expl:
                        store_place.append((new_state, new_path, new_cost,new_direction))
        return None
    
    def dls_search(self,initial_state, goal_state, max_depth = 250):
        storeToPlace = [(initial_state, [initial_state], 0,[])]
        k=0
        nodes = 0 
        while storeToPlace:
            k+=1
            state, path, cost, directions = storeToPlace.pop()
            self.log.info("%s ----- %s ----- %s ------ %s",str(state),str(path),str(cost),str(directions))
            if tuple(map(tuple, state)) == tuple(map(tuple, goal_state)):
                print("Nodes Genarated : ", str(nodes))
                print("Solution found at Depth : ", len(directions))
                print("Cost : ",cost)
                print("Directions for Solution: ")
                for i in directions:
                    print(i)
                self.log.info("Nodes Genarated : %s", str(nodes))
                self.log.info("Solution found at Depth : %s", len(directions))
                self.log.info("Cost : %s",cost)
                self.log.info("Directions for Solution: %s", directions)
                return path
            if cost == max_depth:
                continue
            for a in range(3):
                for b in range(3):
                    if(state[a][b] == 0):
                        i,j = a,b

            gi, gj = i + 0, j - 1
            if 0 <= gi < 3 and 0 <= gj < 3:
                nodes +=1
                new_state = [row.copy() for row in state]
                new_state[i][j] = new_state[gi][gj]
                new_state[gi][gj] = 0
                new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
                new_path = path + [new_state]
                new_direction = directions+["Right "+str(new_state[i][j])]
                storeToPlace.append((new_state, new_path, new_cost,new_direction))
            gi, gj = i + 0, j + 1
            if 0 <= gi < 3 and 0 <= gj < 3:
                nodes +=1
                new_state = [row.copy() for row in state]
                new_state[i][j] = new_state[gi][gj]
                new_state[gi][gj] = 0
                new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
                new_path = path + [new_state]
                new_direction = directions+["Left "+str(new_state[i][j])]
                storeToPlace.append((new_state, new_path, new_cost,new_direction))
            gi, gj = i - 1, j + 0
            if 0 <= gi < 3 and 0 <= gj < 3:
                nodes +=1
                new_state = [row.copy() for row in state]
                new_state[i][j] = new_state[gi][gj]
                new_state[gi][gj] = 0
                new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
                new_path = path + [new_state]
                new_direction = directions+["Down "+str(new_state[i][j])]
                storeToPlace.append((new_state, new_path, new_cost,new_direction))
            gi, gj = i + 1, j + 0
            if 0 <= gi < 3 and 0 <= gj < 3:
                nodes +=1
                new_state = [row.copy() for row in state]
                new_state[i][j] = new_state[gi][gj]
                new_state[gi][gj] = 0
                new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
                new_path = path + [new_state]
                new_direction = directions+["UP "+str(new_state[i][j])]
                storeToPlace.append((new_state, new_path, new_cost,new_direction))
        return None
    
    def ids_search(self,initial_state, goal_state, max_depth = 200):
        for depth in range(100):
            path = self.dls_search(initial_state, goal_state, max_depth)
            if path is not None:
                return path
        return None

    def ucs_search(self, start_state, final_state):
        c=0
        store_place = PriorityQueue()
        store_place.put((0, [start_state], 0,[]))
        expl = set()
        while not store_place.empty():
            c+=1
            _, path, cost, directions = store_place.get()
            state = path[-1]
            self.log.info(" %s-----%s ----- %s ------ %s",str(_),str(path),str(cost),str(directions))
            if tuple(map(tuple, state)) == tuple(map(tuple, final_state)):
                print('Nodes Expanded : ', len(expl))
                print("Nodes Genarated : ", str(c))
                print("Solution found at Depth : ", len(directions))
                print("Cost : ",cost)
                print("Directions for Solution: ")
                for i in directions:
                    print(i)
                self.log.info('Nodes Expanded : %s', len(expl))
                self.log.info("Nodes Genarated : %s", str(c))
                self.log.info("Solution found at Depth : %s", len(directions))
                self.log.info("Cost : %s",cost)
                self.log.info("Directions for Solution: %s", directions)
                return path
            expl.add(tuple(map(tuple, state)))
            directions_rules = {(0,-1):"UP",(0,1):"Down",(-1,0):"Left",(1,0):"Right"}
            i, j = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
            for ti, tj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                gi, gj = i + ti, j + tj
                if 0 <= gi < 3 and 0 <= gj < 3:
                    new_state = [row.copy() for row in state]
                    new_state[i][j] = new_state[gi][gj]
                    new_state[gi][gj] = 0
                    new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
                    new_path = path + [new_state]
                    new_direct = directions + [directions_rules[(ti,tj)]+str(new_state[i][j])]
                    if tuple(map(tuple, new_state)) not in expl:
                        store_place.put((new_cost, new_path, new_cost, new_direct))
                    else:
                        existing_state = next((item for item in store_place.queue if item[1][-1] == new_state), None)
                        if existing_state is not None and new_cost < existing_state[2]:
                            store_place.queue.remove(existing_state)
                            existing_path = existing_state[1]
                            existing_path_cost = existing_state[2]
                            existing_path_cost = new_cost
                            existing_path = new_path
                            store_place.put((existing_path_cost, existing_path, existing_path_cost, new_direct))
        return None

    def greedy_search(self,initial_state, goal_state):
        PQ = PriorityQueue()
        t = sum(1 for i in range(3) for j in range(3) if initial_state[i][j] != goal_state[i][j])
        PQ.put((t, [initial_state], 0,[]))
        explored = set()
        k=0
        nodes =0
        max_Qsize =0
        while not PQ.empty():
            k+=1
            _, path, cost, directions = PQ.get()
            state = path[-1]
            self.log.info(" %s-----%s ----- %s ------ %s",str(_),str(path),str(cost),str(directions))
            if tuple(map(tuple, state)) == tuple(map(tuple, goal_state)):
                print("Nodes Popped : ", k)
                print('Nodes Expanded : ', len(explored))
                print("Nodes Genarated : ", str(nodes))
                print("Max Fringe size : ", str(max_Qsize))
                print("Solution found at Depth : ", len(directions))
                print("Cost : ",cost)
                print("Directions for Solution: ")
                for i in directions:
                    print(i)
                self.log.info("Nodes popped : %s", k)
                self.log.info('Nodes Expanded : %s', len(explored))
                self.log.info("Nodes Genarated : %s", str(nodes))
                self.log.info("Max Fringe size: %s", str(max_Qsize))
                self.log.info("Solution found at Depth : %s", len(directions))
                self.log.info("Cost : %s",cost)
                self.log.info("Directions for Solution: %s", directions)
                return path
            explored.add(tuple(map(tuple, state)))
            for a in range(3):
                for b in range(3):
                    if(state[a][b] == 0):
                        i,j = a,b
            gi, gj = i + 0, j - 1
            if 0 <= gi < 3 and 0 <= gj < 3:
                nodes +=1
                new_state = [row.copy() for row in state]
                new_state[i][j] = new_state[gi][gj]
                new_state[gi][gj] = 0
                new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
                new_path = path + [new_state]
                new_directions = directions + ["Right "+str(new_state[i][j])]
                if tuple(map(tuple, new_state)) not in explored:
                    t = sum(1 for i in range(3) for j in range(3) if new_state[i][j] != goal_state[i][j])
                    PQ.put((t, new_path, new_cost, new_directions))
                    max_Qsize = max(PQ.qsize(),max_Qsize)

            gi, gj = i + 0, j + 1
            if 0 <= gi < 3 and 0 <= gj < 3:
                nodes +=1
                new_state = [row.copy() for row in state]
                new_state[i][j] = new_state[gi][gj]
                new_state[gi][gj] = 0
                new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
                new_path = path + [new_state]
                new_directions = directions + ["Left "+str(new_state[i][j])]
                if tuple(map(tuple, new_state)) not in explored:
                    t = sum(1 for i in range(3) for j in range(3) if new_state[i][j] != goal_state[i][j])
                    PQ.put((t, new_path, new_cost, new_directions))
                    max_Qsize = max(PQ.qsize(),max_Qsize)


            gi, gj = i - 1, j + 0
            if 0 <= gi < 3 and 0 <= gj < 3:
                nodes +=1
                new_state = [row.copy() for row in state]
                new_state[i][j] = new_state[gi][gj]
                new_state[gi][gj] = 0
                new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
                new_path = path + [new_state]
                new_directions = directions + ["Down "+str(new_state[i][j])]
                if tuple(map(tuple, new_state)) not in explored:
                    t = sum(1 for i in range(3) for j in range(3) if new_state[i][j] != goal_state[i][j])
                    PQ.put((t, new_path, new_cost, new_directions))
                    max_Qsize = max(PQ.qsize(),max_Qsize)

            gi, gj = i + 1, j + 0
            if 0 <= gi < 3 and 0 <= gj < 3:
                nodes +=1
                new_state = [row.copy() for row in state]
                new_state[i][j] = new_state[gi][gj]
                new_state[gi][gj] = 0
                new_cost = cost + self.tile_costs_dicts[new_state[i][j]]
                new_path = path + [new_state]
                new_directions = directions + ["UP "+str(new_state[i][j])]
                if tuple(map(tuple, new_state)) not in explored:
                    t = sum(1 for i in range(3) for j in range(3) if new_state[i][j] != goal_state[i][j])
                    PQ.put((t, new_path, new_cost, new_directions))
                    max_Qsize = max(PQ.qsize(),max_Qsize)
        return None
