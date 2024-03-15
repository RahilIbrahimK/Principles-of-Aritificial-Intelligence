MAX, MIN = 1000, -1000
def minmax (depth,nodeindex,maximizingplayer,values,alpha,beta):
    if depth == 3:
        return  values[nodeindex]

    best = MIN if maximizingplayer else MAX
    for i in range(2):
        val = minmax(depth + 1, nodeindex*2+i,not maximizingplayer ,values,alpha,beta)
        best =max(best,val) if maximizingplayer else min(best,val)
        alpha= max(alpha,best) if maximizingplayer else alpha
        beta =min(beta,best) if not maximizingplayer else beta
        if beta <=alpha :
            break
    return best
values = [10,9,14,18,5,4,50,3]
print(" op val =",minmax(0,0,True,values,MIN,MAX))


# def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
#     if depth == 3:
#         return values[nodeIndex]

#     best = MIN if maximizingPlayer else MAX

#     for i in range(2):
#         val = minimax(depth + 1, nodeIndex * 2 + i, not maximizingPlayer, values, alpha, beta)
#         best = max(best, val) if maximizingPlayer else min(best, val)
#         alpha = max(alpha, best) if maximizingPlayer else alpha
#         beta = min(beta, best) if not maximizingPlayer else beta

#         if beta <= alpha:
#             break

#     return best

# if __name__ == "__main__":
#     values = [10, 9, 14, 18, 5, 4, 50, 3]
#     print("The optimal value is:", minimax(0, 0, True, values, MIN, MAX))












# # MAX, MIN =1000,-1000
# # def minimax(depth, nodeIndex, maximizingPlayer, 
# # 			values, alpha, beta): 

# # 	if depth == 3: 
# # 		return values[nodeIndex] 

# # 	if maximizingPlayer: 
	
# # 		best = MIN

# # 		for i in range(0, 2): 
# # 			val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta) 
# # 			best = max(best, val) 
# # 			alpha = max(alpha, best) 

# # 			# Alpha Beta Pruning 
# # 			if beta <= alpha: 
# # 				break
		
# # 		return best 
	
# # 	else:
# # 		best = MAX

# # 		for i in range(0, 2): 
# # 			val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta) 
# # 			best = min(best, val) 
# # 			beta = min(beta, best) 

# # 			# Alpha Beta Pruning 
# # 			if beta <= alpha: 
# # 				break
		
# # 		return best 
	
# # # Driver Code 
# # if __name__ == "__main__": 

# # 	values = [10,9,14,18,5,4,50,3] 
# # 	print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))





# # # import math

# # # # Represents the game tree nodes
# # # class Node:
# # #     def __init__(self, value=None):
# # #         self.value = value
# # #         self.children = []

# # # # Minimax algorithm with alpha-beta pruning
# # # def minimax_alpha_beta(node, depth, alpha, beta, maximizingPlayer):
# # #     if depth == 0 or len(node.children) == 0:
# # #         return node.value
# # #     if maximizingPlayer:
# # #         value = -math.inf
# # #         for child in node.children:
# # #             value = max(value, minimax_alpha_beta(child, depth - 1, alpha, beta, False))
# # #             alpha = max(alpha, value)
# # #             if alpha >= beta:
# # #                 break
# # #         return value
# # #     else:
# # #         value = math.inf
# # #         for child in node.children:
# # #             value = min(value, minimax_alpha_beta(child, depth - 1, alpha, beta, True))
# # #             beta = min(beta, value)
# # #             if beta <= alpha:
# # #                 break
# # #         return value

# # # # Example usage
# # # if __name__ == "__main__":
# # #     # Construct a simple game tree
# # #     root = Node()
# # #     root.value = 3
# # #     node1 = Node()
# # #     node1.value = 5
# # #     root.children.append(node1)
# # #     node2 = Node()
# # #     node2.value = 6
# # #     root.children.append(node2)
# # #     node3 = Node()
# # #     node3.value = 9
# # #     node1.children.append(node3)
# # #     node4 = Node()
# # #     node4.value = 1
# # #     node1.children.append(node4)
# # #     node5 = Node()
# # #     node5.value = 2
# # #     node2.children.append(node5)
# # #     node6 = Node()
# # #     node6.value = 0
# # #     node2.children.append(node6)

# # #     # Perform minimax with alpha-beta pruning
# # #     result = minimax_alpha_beta(root, 3, -math.inf, math.inf, True)
# # #     print("Optimal value:", result)