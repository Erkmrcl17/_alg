def greedy_coordinate_search(X, y, init_params=None, iterations=1000, step=0.1):
    """
    Greedy coordinate-wise search: for each parameter, try small positive/negative moves and accept if improves.
    """
    if init_params is None:
        params = np.zeros(2, dtype=float)
    else:
        params = np.array(init_params, dtype=float)
    best_loss = mse_loss(X, y, params)
    for it in range(iterations):
        improved = False
        for i in range(len(params)):
            for direction in [+1, -1]:
                candidate = params.copy()
                candidate[i] += direction * step
                cand_loss = mse_loss(X, y, candidate)
                if cand_loss < best_loss:
                    params = candidate
                    best_loss = cand_loss
                    improved = True
                    break  # accept first improvement (greedy)
            if improved:
                break
        if not improved:
            # optionally shrink step to fine-tune
            step *= 0.5
            if step < 1e-6:
                break
    return params, best_loss