def gradient_descent_momentum(X, y, init_params=None, lr=0.1, iterations=1000, beta=0.9):
    params = np.zeros(2) if init_params is None else np.array(init_params, dtype=float)
    v = np.zeros_like(params)
    for it in range(iterations):
        grad = compute_gradients(X, y, params)
        v = beta * v + (1 - beta) * grad
        params -= lr * v
    return params, mse_loss(X, y, params)

def rmsprop(X, y, init_params=None, lr=0.01, iterations=1000, beta=0.9, eps=1e-8):
    params = np.zeros(2) if init_params is None else np.array(init_params, dtype=float)
    s = np.zeros_like(params)
    for it in range(iterations):
        grad = compute_gradients(X, y, params)
        s = beta * s + (1 - beta) * (grad ** 2)
        params -= lr * grad / (np.sqrt(s) + eps)
    return params, mse_loss(X, y, params)

def adam(X, y, init_params=None, lr=0.01, iterations=1000, b1=0.9, b2=0.999, eps=1e-8):
    params = np.zeros(2) if init_params is None else np.array(init_params, dtype=float)
    m = np.zeros_like(params)
    v = np.zeros_like(params)
    for t in range(1, iterations+1):
        grad = compute_gradients(X, y, params)
        m = b1 * m + (1 - b1) * grad
        v = b2 * v + (1 - b2) * (grad ** 2)
        m_hat = m / (1 - b1**t)
        v_hat = v / (1 - b2**t)
        params -= lr * m_hat / (np.sqrt(v_hat) + eps)
    return params, mse_loss(X, y, params)