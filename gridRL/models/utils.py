import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def make_image(matrix : np.ndarray):
    df_transposed = pd.DataFrame(np.transpose(matrix))
    print(df_transposed)
    return df_transposed


def save_result(df : pd.DataFrame, iteration):
    df.to_csv(f'result after {iteration} iteration.csv',index=False)


def visualize(history, model, env, n_episodes, total_reward):
    if env=='cliff':
        width = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        height = [0, 1, 2, 3, 4]

        plt.figure(figsize=(9, 5))
        plt.grid()
        plt.fill_between(width[1:8], 3, 4, color='grey')
        plt.text(4, 3.5, 'Cliff', color='brown', fontsize=40, ha='center', va='center')

        x_values = [item[0] for item in history]
        y_values = [item[1] for item in history]
        plt.plot(x_values, y_values, markersize=10,marker='o', linewidth=4, color = 'purple')

        plt.gca().invert_yaxis()  # Invert y-axis
        plt.yticks(height)
        plt.xticks(width)
        plt.savefig(f'../../plots/{model}_{env}_{n_episodes}episodes_{total_reward}score.png')


    elif env =='maze':
        width = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        height = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        plt.figure(figsize=(13, 9))
        plt.grid()
        plt.fill_between(range(1,5),1,4, color='grey')
        plt.text(2.5, 2.5, 'Cliff', color='brown', fontsize=40, ha='center', va='center')

        plt.fill_between(range(2,4),6,8, color='grey')
        plt.text(3, 7, 'Cliff', color='brown', fontsize=40, ha='center', va='center')

        plt.fill_between(range(10,13),5,6, color='grey')
        plt.text(11.5, 5.5, 'Cliff', color='brown', fontsize=40, ha='center', va='center')

        plt.fill_between(range(4,8),4,5, color='grey')
        plt.fill_between(range(5, 8), 5, 6, color='grey')
        plt.fill_between(range(6, 8), 6, 7, color='grey')

        plt.fill_between(range(7, 11), 3, 4, color='grey')
        plt.fill_between(range(7, 10), 2, 3, color='grey')
        plt.fill_between(range(7, 9), 1, 2, color='grey')
        plt.text(7, 4 , 'Cliff', color='brown', fontsize=40, ha='center', va='center')

        plt.plot([3,4,5,6], [4,5,6,7], alpha = 0.5, linewidth=10, color = 'skyblue')
        plt.plot([7,8,9,10], [0,1,2,3], alpha = 0.5, linewidth=10, color = 'skyblue')


        x_values = [item[0] for item in history]
        y_values = [item[1] for item in history]
        plt.plot(x_values, y_values, markersize=10,marker='o', linewidth=4, color = 'purple')

        plt.gca().invert_yaxis()  # Invert y-axis
        plt.yticks(height)
        plt.xticks(width)
        plt.savefig(f'../../plots/{model}_{env}_{n_episodes}episodes_{total_reward}score.png')




def export_image(env, model, n_episodes, image):
    pass
