import numpy as np

final_path = "src/comtraq-mpc/data/first_optimal_path_with_yaw_2.npy"
v = 0  # initial velocity
dt = 0.2  # time step
path_index = 0  # initial path index
goal = final_path[-1]  # goal position
budget = 20  # initial budget
buffer_size = 10000  # Size of the replay buffer
learning_rate = 1e-3  # Learning rate
batch_size = 128  # Size of the batch for learning
gamma = 0.9  # Discount factor
exploration_fraction = 0.76  # Fraction of entire training period over which the exploration rate is reduced
exploration_final_eps = 0.02  # Final value of random action probability
target_update_interval = (
    1000  # Number of steps after which the target network is updated
)
train_freq = (1, "episode")  # Update the model every 'train_freq' steps
gradient_steps = -1  # Number of gradient steps to take after each environment step
log_dir = "tmp/dqn/"  # Where to log the model
total_timesteps = 300000  # total number of timesteps to train the model
map_name = "dronelab"

model_path = f"src/comtraq-mpc/trained_models/dqn_communication_optimization_epsfrac08_steps{int(total_timesteps/1000)}k_turtlebot_path_budget{budget}_{map_name}"  # path to save the model

