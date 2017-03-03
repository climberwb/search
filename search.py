# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  # util.raiseNotDefined()
  # print(dir(problem))
  # print "Start:", problem.getStartState()
  # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  # print "Start's successors:", problem.getSuccessors(problem.getStartState())
  # print problem.walls
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST
  # print dir(problem)
  # print(problem.isGoalState(problem.getStartState()))
  # if problem.isGoalState(problem.getStartState()) or 'actions'in dir(problem) and len(problem.actions)>12:
  #   print problem._visitedlist
  #   return [v for v in problem.actions]
  # for direction in problem.getSuccessors(problem.getStartState()):
  #   if direction[0] not in problem._visitedlist:
  #     problem._visitedlist+=[direction[0]]
  #     problem.startState = direction[0]
  #     if'actions'in dir(problem):
  #       problem.actions += [direction[1]]
  #     else:
  #       problem.actions = [direction[1
  if problem.isGoalState(problem.getStartState()):
    return []
 
  frontier = util.Stack()
  visited = set()
  start_state = problem.getStartState() #
  frontier.push(start_state)# [((1,4),...]
  visited.add(start_state)
  path={}
  while not frontier.isEmpty():
   
    parent = frontier.pop()
    successor_states = problem.getSuccessors(parent)
    for child_state in successor_states:
     
      pos,action,cost = child_state
      if pos in visited:
        continue
      visited.add(pos)
      path[child_state[0]] = (parent,child_state[1])
         #child_state
      # print visited
      if problem.isGoalState(pos):
        path_arr=[]
        current_node = child_state[0]
        # import pprint
        # pp = pprint.PrettyPrinter(indent=4)
        # print  pp.pprint(path)
        while start_state != current_node:
        # for i in range(0,10):
          # print 'iter'
          direction = path[current_node][1]
          # print direction , parent
          path_arr.append(direction)
          current_node = path[current_node][0]
        # print path_arr
        return path_arr[::-1]
      # print(pos,problem.getSuccessors(problem.getStartState())[::-1])
      frontier.push(pos)
      # path.append(problem.getSuccessors(problem.getStartState()))





def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  # print "Start:", problem.getStartState()
  # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  # print "Start's successors:", problem.getSuccessors(problem.getStartState())
  # print(dir(problem))
  # from game import Directions
  # s = Directions.SOUTH
  # w = Directions.WEST
  # return  [s,s,w,s,w,w,s,w]
  # if problem.isGoalState(problem.getStartState()):
  #   return []
 
  # frontier = util.Stack()
  frontier = []
  visited = set()
  start_state = problem.getStartState() #
  frontier.append(start_state)# [((1,4),...]
  visited.add(start_state)
  path={}
  while frontier !=[]:
   #########################
    parents = frontier
    frontier = []

   #########################
    for parent in parents:  
      successor_states = problem.getSuccessors(parent)
      for child_state in successor_states:
        ############
        print('in for')
        ###########
        # TODO 1. nested for loop that goes over all
        #      2. loops over children of frontier
        #      3. adds children to frontier unless children have been visted
        #      4. adds action to path 
        pos,action,cost = child_state
        if pos in visited:
          continue
        visited.add(pos)
        path[child_state[0]] = (parent,child_state[1])
           #child_state
        # print visited
        if problem.isGoalState(pos):
          print("goal!!")
          path_arr=[]
          current_node = child_state[0]
          import pprint
          pp = pprint.PrettyPrinter(indent=4)
          print  pp.pprint(path)
          while start_state != current_node:
          # for i in range(0,10):
            # print 'iter'
            direction = path[current_node][1]
            # print direction , parent
            path_arr.append(direction)
            current_node = path[current_node][0]
          # print path_arr
          return path_arr[::-1]
        # print(pos,problem.getSuccessors(problem.getStartState())[::-1])
          print('in for')
        frontier.append(pos)

  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
