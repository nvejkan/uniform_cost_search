# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 21:34:07 2018

@author: nattawutvejkanchana
"""

from graph import *

def solution(node):
    
    if node.parent is None:
        return [str(node)]
    else:
        l = solution(node.parent)
        l.append(str(node))
        return l

def uniform_cost_search(problem):
    node = Node(problem.get_init_state(),0)
    frontier = [node]
    explored = dict()
    while(True):
        if len(frontier) == 0:
            print("Failure")
            return False
            
        node = frontier.pop(0)
        
        if problem.get_goal_state() == node.state:
            return solution(node)
        
        #check to add node to explored
        explored[node.state] = node.cost
        for action in problem.get_actions(node.state):
            child = problem.child_node(node,action)
            if (not child.state in explored.keys() \
                or (child.state in explored.keys() and child.cost < explored.get(child.state))):
                    frontier.append(child)
                    frontier.sort()

#test
probA = Path_problem(graph_A,"S","B")
sol = uniform_cost_search(probA)

#https://algorithmicthoughts.wordpress.com/2012/12/15/artificial-intelligence-uniform-cost-searchucs/
graph_2 = { "S": [("A",1),("G",12)]
, "A": [("B",3),("C",1),("S",1)]
, "B": [("A",3),("D",3)]
, "C": [("A",1),("D",1),("G",2)]
, "D": [("B",3),("C",1),("G",3)]
, "G": [("S",12),("C",2),("D",3)]
}

probB = Path_problem(graph_2,"S","G")
sol = uniform_cost_search(probB)
                
        
