from queue import PriorityQueue
from collections import deque
import sys
import logging
from searchalgos import Searchalgo
from datetime import date,datetime
sys.setrecursionlimit(5500)

args = sys.argv
inputFile = sys.argv[1]
outputFile = sys.argv[2]
algo = "astar"
need_logs = False
if(len(sys.argv) >3):
    if sys.argv[3] not in ["true","false"]:
        algo = sys.argv[3]
        flage = [True if sys.argv[4]=="true" else False]
    else:
        if sys.argv[3] == "true":
            need_logs = True
        else:
            need_logs = False
else:
    algo = "astar"
    need_logs = False

if(len(sys.argv) > 4):
    if sys.argv[4] == "true":
        need_logs = True
    else:
        need_logs = False

initial_state = []
f = open(inputFile,'r')
d = f.read()
k = d.split('\n')[:-1]
for i in k:
    t = []
    for j in i.split(' '):
        t.append(int(j))
    initial_state.append(t)
f.close()

goal_state = []
f = open(outputFile,'r')
d = f.read()
k = d.split('\n')[:-1]
for i in k:
    t = []
    for j in i.split(' '):
        t.append(int(j))
    goal_state.append(t)
f.close()

if need_logs:
    v=datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    logging.basicConfig(filename=v, filemode='w', format='%(name)s - %(message)s',level=logging.INFO)
if algo == "a*":
    algo = "astar"
algo = algo + "_search"
s = Searchalgo(logging)
m = getattr(s,algo)
path = m(initial_state, goal_state)
if(path != None):
    for i in path:
        print(i)
else:
    print("NO Solution found")
