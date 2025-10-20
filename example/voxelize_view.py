import argparse
import numpy as np
from Bio.PDB import PDBParser
import matplotlib.pyplot as plt


def load_atoms(pdb_file):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('model', pdb_file)
    coords = [atom.get_coord() for atom in structure.get_atoms()]
    return np.array(coords)


def voxelize(coords, voxel_size=1.0, padding=2.0):
    """Voxelize atomic coordinates.

    Parameters
    ----------
    coords : np.ndarray
        Array of atomic coordinates with shape (N, 3).
    voxel_size : float, optional
        Side length of each voxel in angstroms.
    padding : float, optional
        Extra padding added around the bounding box.

    Returns
    -------
    np.ndarray
        Boolean 3D array representing occupied voxels.
    tuple
        Origin of the grid.
    float
        Voxel size used for discretization.
    """
    min_c = coords.min(axis=0) - padding
    max_c = coords.max(axis=0) + padding
    grid_size = np.ceil((max_c - min_c) / voxel_size).astype(int)
    voxels = np.zeros(grid_size, dtype=bool)
    indices = np.floor((coords - min_c) / voxel_size).astype(int)
    valid = ((indices >= 0) & (indices < grid_size)).all(axis=1)
    indices = indices[valid]
    voxels[indices[:, 0], indices[:, 1], indices[:, 2]] = True
    return voxels, min_c, voxel_size


def visualize(voxels):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(voxels, edgecolor='k', facecolors='cyan', alpha=0.7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(description='Voxelize PDB and visualize.')
    parser.add_argument('pdb', help='Input PDB file')
    parser.add_argument('--size', type=float, default=1.0, help='Voxel size in angstroms')
    args = parser.parse_args()

    coords = load_atoms(args.pdb)
    voxels, origin, voxel_size = voxelize(coords, voxel_size=args.size)
    visualize(voxels)


if __name__ == '__main__':
    main()
