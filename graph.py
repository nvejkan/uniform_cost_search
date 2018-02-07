# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 20:45:34 2018

@author: nattawutvejkanchana
"""

class Node():
    def __init__(self,state,cost=0,parent=None):
        self.state = state
        self.cost = cost
        self.parent = parent
    
    def __str__(self):
        return "{0}:{1}".format(self.state,self.cost)
    
    def __lt__(self, other):
        return self.cost < other.cost
    def __le__(self, other):
        return self.cost <= other.cost
    def __eq__(self, other):
        return self.cost == other.cost
    def __ne__(self, other):
        return self.cost != other.cost
    def __gt__(self, other):
        return self.cost > other.cost
    def __ge__(self, other):
        return self.cost >= other.cost
    
        
class Path_problem():
    def __init__(self,graph,start_node,goal_node):
        self.graph = graph
        self.start_node = start_node
        self.goal_node = goal_node
        
    def get_init_state(self):
        return self.start_node
    
    def get_goal_state(self):
        return self.goal_node
    
    def get_actions(self,state):
        #actions = walk along the paths
        return self.graph.get(state)
        
    def child_node(self,parent_node,action):
        #e.g. action = ('B', 211) 
        child = Node(action[0],parent_node.cost+action[1],parent_node)
        return child
    
    
        

#graph
graph_A = { "S": [("F",99),("R",80)]
, "F": [("B",211),("S",99)]
, "R": [("P",97),("S",80)]
, "P": [("B",101),("R",97)]
, "B": [("P",101),("F",211)]
}
        
