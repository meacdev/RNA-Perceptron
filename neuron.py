class Neuron:
    def __init__(self, dataset):
        self.dataset = dataset
        self.X = np.insert(dataset[:, :-1], 0, 1, axis=1)
        self.Yd = dataset[:, -1]
        self.weights = np.zeros(3, dtype=int)
        self.learning_rate = 0.1
        self.w_adjust_count = 0
        self.epochs = 0
        self.w_changes = np.empty((0, 3))

    def threshold(self, inputs, weights):
        if len(inputs) != len(weights):
            raise ValueError("O vetor de entradas deve ter a mesma quantidade de elementos que o de pesos")
        v = 0.0
        for i in range(len(inputs)):
            v += inputs[i] * weights[i]
        if v < 0:
            return 0
        else:
            return 1

    def adjust_weights(self, inputs, weights, error):
        return weights + self.learning_rate * error * inputs

    def train(self, inputs, targets):
        print(f"Vetor inicial de pesos: {self.weights}")
        while True:
            had_error = False
            for xi, yi in zip(inputs, targets):
                output = self.threshold(xi, self.weights)
                error = yi - output
                if error != 0:
                    had_error = True
                    self.w_changes = np.vstack((self.w_changes, self.weights))
                    self.weights = self.adjust_weights(xi, self.weights, error)
                    self.w_adjust_count += 1
            self.epochs += 1
            if not had_error:
                break

    def execute(self):
        self.train(self.X, self.Yd)
        print(f"Vetor final de pesos: {self.weights}")
        print(f"Número total de ajustes no vetor de pesos: {self.w_adjust_count}")
        print(f"Número de épocas até a convergência: {self.epochs}")
        self.plot()

    def plot(self):
        w0, w1, w2 = self.weights

        y0 = self.X[self.Yd == 0]
        y1 = self.X[self.Yd == 1]
        
        plt.scatter(y0[:, 1], y0[:, 2], color="red", label="Classe 0", s=20)
        plt.scatter(y1[:, 1], y1[:, 2], color="blue", label="Classe 1", s=20)

        x = np.array([self.X[:, 1].min(), self.X[:, 1].max()])
        y = -(w0 + w1 * x) / w2
        
        plt.plot(x, y, color="purple", label="Reta que separa as classes")
        plt.xlabel("x1")
        plt.ylabel("x2")
        plt.legend()
        plt.show()