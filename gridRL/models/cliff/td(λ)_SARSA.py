from gridRL.env.cliffenv import Cliffenv
from gridRL.models.utils import *

class Agent():

    def __init__(self):
        self.action_grid = [[-1,0],[1,0],[0,-1],[0,1]] # left, right, up, down
        self.action_grid_txt = [['left'],['right'],['up'],['down']]
        self.width = 9
        self.height = 5
        self.qtable = np.zeros((self.width , self.height, len(self.action_grid)))
        self.e_trace = np.zeros((self.width , self.height, len(self.action_grid)))
        self.epsilon = 1
        self.gamma = .95
        self.lr = .01
        self.n_episode = 1
        self.memory = []

    def get_q_values(self, state):
        q_values = self.qtable[tuple(state)]
        return q_values
    def sample_action(self, state):
        self.epsilon = self.update_epsilon()
        self.n_episode +=1

        if self.epsilon > np.random.rand():
            action_idx = np.random.choice(range(len(self.action_grid)), 1)[0]
        else:
            q_values = self.get_q_values(state)
            q_max = np.amax(q_values)
            tie_Qchecker = np.where(q_values == q_max)[0]

            if len(tie_Qchecker) >1:
                action_idx = np.random.choice(tie_Qchecker,1)[0]
            else:
                action_idx = np.argmax(q_values)

        action = self.action_grid[action_idx]

        return action
    def update_epsilon(self):
        return self.epsilon / self.n_episode

    def update(self, state, action, reward, state_, action_):
        action_idx = self.action_grid.index(action)
        action_idx_ = self.action_grid.index(action_)

        self.e_trace[tuple(state)][action_idx] += self.gamma * 1
        next_q_value = self.qtable[tuple(state_)][action_idx_]

        delta = reward + self.gamma * next_q_value
        self.qtable[tuple(state)][action_idx] += self.lr * delta * self.e_trace[tuple(state)][action_idx]
    def save_state_memory(self, state):
        self.memory.append(state)
    def clear_state_memory(self):
        self.memory = []

if __name__ == '__main__':
    env = Cliffenv()
    agent = Agent()
    n_games = 200

    for game in range(n_games):

        total_reward = 0
        walk = 0
        state = env.reset()
        action = agent.sample_action(state)
        while True:
            agent.save_state_memory(state)

            state_,reward, done = env.step(state, action)
            action_ = agent.sample_action(state_)

            agent.update(state, action, reward, state_, action_) # S, A, R, S_, A_
            total_reward += reward
            # action_ = agent.sample_action(state_)

            if done:
                if game == n_games-1:
                    agent.save_state_memory(state_)
                    result_route = agent.memory
                    print(f'Final Route : {result_route}')
                    visualize(agent.memory, 'td(λ)_SARSA', 'cliff', n_games, total_reward)
                agent.clear_state_memory()
                print(f'{game}episode ended!! Total reward : {total_reward}')
                break

            state = state_
            action = action_
            walk += 1

