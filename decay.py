import numpy as np

def simulate(n_atoms, decay_prob):
    atoms = n_atoms
    history = [atoms]
    while atoms > 0:
        decays = np.random.binomial(atoms, decay_prob)
        atoms -= decays
        history.append(atoms)
    return history
