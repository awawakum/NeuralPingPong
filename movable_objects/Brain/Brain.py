import numpy as np


class Brain:

    INPUT_DIM = 4
    OUT_DIM = 3
    H_DIM = 6

    W1 = np.random.rand(INPUT_DIM, H_DIM)
    b1 = np.random.rand(1, H_DIM)
    W2 = np.random.rand(H_DIM, OUT_DIM)
    b2 = np.random.rand(1, OUT_DIM)

    W1 = (W1 - 0.5) * 2 * np.sqrt(1 / INPUT_DIM)
    b1 = (b1 - 0.5) * 2 * np.sqrt(1 / INPUT_DIM)
    W2 = (W2 - 0.5) * 2 * np.sqrt(1 / H_DIM)
    b2 = (b2 - 0.5) * 2 * np.sqrt(1 / H_DIM)

    ALPHA = 0.0001

    loss_arr = []

    def clear_data(self):
        self.W1 = np.random.rand(self.INPUT_DIM, self.H_DIM)
        self.b1 = np.random.rand(1, self.H_DIM)
        self.W2 = np.random.rand(self.H_DIM, self.OUT_DIM)
        self.b2 = np.random.rand(1, self.OUT_DIM)

        self.W1 = (self.W1 - 0.5) * 2 * np.sqrt(1 / self.INPUT_DIM)
        self.b1 = (self.b1 - 0.5) * 2 * np.sqrt(1 / self.INPUT_DIM)
        self.W2 = (self.W2 - 0.5) * 2 * np.sqrt(1 / self.H_DIM)
        self.b2 = (self.b2 - 0.5) * 2 * np.sqrt(1 / self.H_DIM)

    def train(self, x, y):
        # Forward
        t1 = x @ self.W1 + self.b1
        h1 = self.relu(t1)
        t2 = h1 @ self.W2 + self.b2
        z = self.softmax(t2)

        E = np.sum(self.sparse_cross_entropy(z, y))

        # Backward
        y_full = self.to_full(y, self.OUT_DIM)
        dE_dt2 = z - y_full

        dE_dW2 = h1.T @ dE_dt2
        dE_db2 = np.sum(dE_dt2, axis=0, keepdims=True)
        dE_dh1 = dE_dt2 @ self.W2.T
        dE_dt1 = dE_dh1 * self.relu_deriv(t1)
        dE_dW1 = x.T @ dE_dt1
        dE_db1 = np.sum(dE_dt1, axis=0, keepdims=True)

        # Update
        self.W1 = self.W1 - self.ALPHA * dE_dW1
        self.b1 = self.b1 - self.ALPHA * dE_db1
        self.W2 = self.W2 - self.ALPHA * dE_dW2
        self.b2 = self.b2 - self.ALPHA * dE_db2

        self.loss_arr.append(E)


    def softmax_batch(self, t):
        out = np.exp(t)
        return out / np.sum(out, axis=1, keepdims=True)

    def relu(self, t):
        return np.maximum(t, 0)

    def softmax(self, t):
        out = np.exp(t)
        return out / np.sum(out)

    def sparse_cross_entropy(self, z, y):
        return -np.log(z[0, y])

    def sparse_cross_entropy_batch(self, z, y):
        return -np.log(np.array([z[j, y[j]] for j in range(len(y))]))

    def to_full_batch(self, y, num_classes):
        y_full = np.zeros((len(y), num_classes))
        for j, yj in enumerate(y):
            y_full[j, yj] = 1
        return y_full

    def to_full(self, y, num_classes):
        y_full = np.zeros((1, num_classes))
        y_full[0, y] = 1
        return y_full

    def relu_deriv(self, t):
        return (t >= 0).astype(float)

    def predict(self, x):
        t1 = x @ self.W1 + self.b1
        h1 = self.relu(t1)
        t2 = h1 @ self.W2 + self.b2
        z = self.softmax(t2)
        return z

    def get_lossArr(self):
        return self.loss_arr

