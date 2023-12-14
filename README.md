#  OverView

 - Environments 
	 - 
	 1. Cliff Environment
	 2. Maze Environment 
 - Models 
	 - 

	 1. MC ( need update ) 
	 2. Q-learning
	 3. SARSA
	 4. td(λ)-Q
	 5. td(λ)-SARSA



 - Conclusion 
	 - 
**Cliff**
|Models|200|300|500|
|------|---|---|---|
|Q-learning|76|86|91*
|SARSA|63|81|91*
|td(λ)-Q|91|91|91
td(λ)-SARSA|91|91|91


**MAZE**
|Models|7500|8000|
|------|---|---|
|td(λ)-Q|-101|89*|
|td(λ)-SARSA|89*|89*|

 - Plots 
	 - 
1. Q-learning - 300episodes
![Qlearning_cliff_300episodes_86score](https://github.com/Sigma-Flip/Basic-RL-models--/assets/138303561/3bc88be1-688f-4c09-9a71-b4d590e1061e)
2. SARSA - 500 episodes
![SARSA_cliff_500episodes_91score](https://github.com/Sigma-Flip/Basic-RL-models--/assets/138303561/bef99199-f75b-4be5-b073-8e1a895e4d0f)

3. td(λ)-Q - 8000 episodes
![td(λ)_Qlearning_maze_8000episodes_89score](https://github.com/Sigma-Flip/Basic-RL-models--/assets/138303561/4fa1f7f8-5884-489d-a908-ef3a479b6362)


 - version
	
	

> `python 1.26.2`
