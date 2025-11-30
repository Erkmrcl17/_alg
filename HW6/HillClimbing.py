import numpy as np

def mse_loss(X, y, params):
    # params = [w0, w1]
    preds = params[0] + params[1] * X
    return np.mean((preds - y) ** 2)

def hill_climbing(X, y, init_params=None, iterations=5000, step_scale=0.1, seed=None):
    """
    Hill climbing: random neighbor search.
    step_scale controls neighbor perturbation scale.
    """
    rng = np.random.RandomState(seed)
    if init_params is None:
        params = rng.randn(2)  # [w0, w1]
    else:
        params = np.array(init_params, dtype=float)
    best_loss = mse_loss(X, y, params)
    for it in range(iterations):
        # propose neighbor
        candidate = params + rng.normal(scale=step_scale, size=params.shape)
        cand_loss = mse_loss(X, y, candidate)
        if cand_loss < best_loss:
            params, best_loss = candidate, cand_loss
    return params, best_loss