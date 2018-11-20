#pseudo
#mcts for selecting decending tree and selecting best node
#NN for predicting what states/actions are worth visiting
#for every state value and visit_count is saved ; not a lot of memory needed bc only a "few" states visited

#def monte_carlo_tree_search(root):
#    while resources_left(time, computational power):
#        leaf = traverse(root) # leaf = unvisited node 
#        simulation_result = rollout(leaf)
#        backpropagate(leaf, simulation_result)
#    return best_child(root)
#

visits=np.zeros((available_actions,0)

def mcts(state):
    while 1:
    state_new = update(state simulation_result_reward://www.twitch.tv/sodapoppin)
        reward = rollout(state_new)
        backpropagate(state_new,reward)
    return best_action(state)


#def traverse(node):
#    while fully_expanded(node):
#        node = best_uct(node)
#    return pick_univisted(node.children) or node # in case no children are present / node is terminal 

def update(state):
    if 
    action=pickaction(state)
    state_new=move(state,action)
    return state_new
#
#def rollout(node):
#    while non_terminal(node):
#        node = rollout_policy(node)
#    return result(node) 
#
#def rollout_policy(node):
#    return pick_random(node.children)
#
#def backpropagate(node, result):
#   if is_root(node) return 
#   node.stats = update_stats(node, result) 
#   backpropagate(node.parent)
#
#def best_child(node):
#    pick child with highest number of visits




# def mtcs(state)
#   state.visits+=1
#   if all state.child visits>1:
#       child = max(value_funtion(state))
#       mtcs(child)
#   else:
#       if some state.child visits=0:
#           child = select random unvisited child
#       else:
#           child = state
#       reward = random_playout(child)
#   update_value(state,reward)
