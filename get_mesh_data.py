import trimesh
import sys

import argparse

parser = argparse.ArgumentParser("mesh info extractor")
parser.add_argument("filename", type=str)
args = parser.parse_args()

filename = args.filename

mesh = trimesh.load(filename)
print("Loaded mesh from", filename, "=", mesh)

to_origin, extent = trimesh.bounds.oriented_bounds(mesh)
print("pos =", to_origin[:3, 3])
# Trimesh does things in the "wrong" order
#w, x, y, z = trimesh.transformations.quaternion_from_matrix(to_origin)
#orn = [x, y, z, w]
orn = trimesh.transformations.euler_from_matrix(to_origin)
print("orn =", orn)
print("extents =", extents)
