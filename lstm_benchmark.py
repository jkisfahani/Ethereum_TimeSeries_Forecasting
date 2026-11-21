import time
import torch
import numpy as np

# Optimize CPU threading for the older dual-core processor
torch.set_num_threads(1)
torch.set_num_interop_threads(1)

print("PyTorch CPU threads:", torch.get_num_threads())

print("PyTorch version:", torch.__version__)
print("NumPy version:", np.__version__)

# Reproducibility
torch.manual_seed(42)
np.random.seed(42)

# Synthetic time-series data
X = torch.randn(500, 30, 3)
y = torch.randn(500, 1)

# Train/test split
X_train = X[:400]
y_train = y[:400]

# Small LSTM model
class LSTMModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = torch.nn.LSTM(
            input_size=3,
            hidden_size=16,
            num_layers=1,
            batch_first=True
        )
        self.fc = torch.nn.Linear(16, 1)

    def forward(self, x):
        output, _ = self.lstm(x)
        return self.fc(output[:, -1, :])

model = LSTMModel()

criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training benchmark
start_time = time.time()

for epoch in range(10):
    model.train()

    optimizer.zero_grad()

    predictions = model(X_train)
    loss = criterion(predictions, y_train)

    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch + 1}/10 - Loss: {loss.item():.6f}")

elapsed_time = time.time() - start_time

print("\nBenchmark completed.")
print(f"Training time: {elapsed_time:.2f} seconds")
print(f"Time per epoch: {elapsed_time / 10:.2f} seconds")