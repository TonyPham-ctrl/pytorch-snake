Credit: Patrick Loeber for inspiration, example game.py model and theory, his github can be found  https://github.com/patrickloeber

Goal: design an AI that plays snakes using PyTorch library


Program demonstrates Reinforcement Learning(RL) - machine learning involving 'agents' that takes actions in a specific environment to maximise 'reward'
this program uses deep neural network(Deep Q) to predict the next optimal action of the agent

To play, run 'agent.py'

Reward: +10 for each apple ate, -10 for every death
Action: [straight, right, left] -> depends on current direction of the head -> bool
State: [dangerStraight, dangerRight, dangerLeft, directionLeft, directionRight, directionUp, directionDown, foodLeft, foodRight, foodUp, foodDown] -> bool
state(11 different bool value) array is inputted as 'INPUT' in the model and the predicted action (3 num) is outputted


Q val = quality of action

1. choose action using .predict(state)
2. perform action
3. measure reward
4. updated Q value and train model

utilises Bellman equation to calculate loss function:
s = state, a = action
newQ(s,a) = currQ(s,a) + learningRate[reward(s,a) + discount*maxExpectedReward(s',a')]

currQ = model.predict(state0)
newQ = reward(s,a) + discount["gamma"]*max(Q(state1))

loss Funciton: loss = (newQ - Q)^2 -> mean squared error