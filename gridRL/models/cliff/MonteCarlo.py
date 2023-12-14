from gridRL.env.cliffenv import Cliffenv
from gridRL.models.utils import *


class Agent:

    def __init__(self):
        self.action_grid = [[-1,0], [1,0], [0,-1], [0,1]] # left, right, up, down
        self.width = 9
        self.height = 5
        self.value_table = np.zeros((self.width, self.height)) # width * height
        self.gamma = 0.95
        self.lr = 0.01
        self.memory = []
        self.epsilon = 1
        self.n_episode = 1

    def update_epsilon(self):
        return self.epsilon / self.n_episode

    def sample_action(self, state):
        self.epsilon = self.update_epsilon()
        self.n_episode +=1

        if self.epsilon > np.random.rand():
            action_idx = np.random.choice(len(self.action_grid),1)[0]
        else:
            state_values = np.array([])
            for state_ in self.next_states(state):
                state_value = self.value_table[tuple(state_)]
                state_values = np.append(state_values, state_value)
            max_value = np.amax(state_values)
            tie_sChecker = np.where(state_values == max_value)[0]

            if len(tie_sChecker) >1:
                action_idx = np.random.choice(tie_sChecker,1)[0]
            else:
                action_idx = np.argmax(state_values)

        action = self.action_grid[action_idx]
        self.epsilon -= .00001

        return action
    def next_states(self, state):
        next_states = []
        x,y =  state
        for idx in range(len(self.action_grid)):
            x += self.action_grid[idx][0]
            y += self.action_grid[idx][1]

            if x < 0:
                x = 0
            elif x > self.width - 1:
                x = self.width -1

            if y < 0:
                y = 0
            elif y > self.height -1:
                y = self.height -1

            next_states.append([x,y])

        return next_states

    # def update(self):
    #     G_t = 0
    #     V_t = 0
    #     visited_state = []
    #     print('memory : ', self.memory)
    #     for state, reward in reversed(self.memory):
    #
    #         if state not in visited_state:
    #             visited_state.append(state)
    #             G_t = self.gamma * G_t + reward
    #             V_t = V_t  + self.lr*( G_t - V_t)
    #             print(f'state: {state}, reward: {reward}, V_t: {V_t}')
    #
    #             self.value_table[(tuple(state))] = V_t

    def update(self):
        G_t = 0
        visited_state = []

        for state, reward in reversed(self.memory):
            G_t = self.gamma * G_t + reward

            if state not in visited_state:
                visited_state.append(state)
                self.value_table[tuple(state)] += self.lr * (G_t - self.value_table[tuple(state)])

    def save_memory(self, state, reward):
        self.memory.append([state, reward])
    def save_state(self, state_seq, action):
        state_seq.append(action)

    def clear_memory(self):
        self.memory = []

if __name__ == '__main__':
    n_episodes = 300
    env = Cliffenv()
    agent = Agent()



    for episode in range(n_episodes):
        state = env.reset()
        action = agent.sample_action(state)
        state_seq = []
        total_reward = 0
        sr = 0
        walk = 0
        while True:
            # print(f'state for {walk}walk: ', state)
            # print(f'action: {walk}walk', action)
            agent.save_state(state_seq, state)
            state_, reward, done = env.step(state, action)
            agent.save_memory(state_, reward)
            print('state : ', state_)


            total_reward += reward
            action = agent.sample_action(state_)
            state = state_
            walk += 1
            if done:
                agent.save_state(state_seq, state_)
                print(agent.memory)


                print(f'{episode}episode,  reward: {total_reward}, state_seq: {state_seq}')
                sr += 1
                agent.update()
                agent.clear_memory()

                break

    df = make_image(agent.value_table)
    # save_result(df, n_episodes)
    visualize(agent.memory, 'MC', 'cliff', n_episodes, total_reward)









