import rubik
import Queue
from collections import OrderedDict


def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    forwardStates = OrderedDict()
    backStates = OrderedDict()
    q = Queue.Queue()
    forwardStates[start] = []
    backStates[end] = []
    q.put(start)
    q.put(end)
    if(start == end):
	return ()
    while(not q.empty()):
	current = q.get()
 
	for x in rubik.quarter_twists:

		t = rubik.perm_apply(x, current)
		

		if(current in forwardStates):
			if(t in forwardStates):
				continue
			if(len(forwardStates[current]) >= 7):
				return
			forwardStates[t] = list(forwardStates[current])
			forwardStates[t].append(x)
				
			if(t in backStates):
				return getPath(forwardStates[t],backStates[t])
			else:
				q.put(t)
			
		else:
			if t in backStates:
				continue
			if(len(backStates[current]) >= 7):
				return
			backStates[t] = list(backStates[current])
			backStates[t].append(x)
			if(t in forwardStates):
				return getPath(forwardStates[t], backStates[t])
			else:
				q.put(t)
	
	
def getPath(beg, end):
	end.reverse()
	for x in end:
		beg.append(rubik.perm_inverse(x))
	return beg
	


