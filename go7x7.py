from CNN import Net
from az_parallel2 import AlphaZeroParallel2
from go import GoBoard
from torch.optim import Adam

G7_MODEL_PARAMS = {"size":7, "action_size":7**2+1, "num_resBlocks":20, "num_hidden":64} 
G7_TRAIN_PARAMS = {"n_iterations":10, "self_play_iterations":100, "mcts_iterations":200, "n_epochs":20, "batch_size":128, "n_self_play_parallel":20, "move_cap":7**2.5}

def train():
    model = Net(**G7_MODEL_PARAMS)
    board = GoBoard(7)
    optimizer = Adam(model.parameters(), lr=0.01, weight_decay=0.0001)
    Alpha = AlphaZeroParallel2(model, optimizer, board, 'G', data_augmentation=True, **G7_TRAIN_PARAMS)
    Alpha.Learn()

train()