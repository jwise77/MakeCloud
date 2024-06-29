import sys
import os
import napari
import h5py as h5
import numpy as np

if len(sys.argv) < 2:
    raise RuntimeError(f'usage: python {sys.argv[0]} datafile')
fn = sys.argv[-1]
if not os.path.exists(fn):
    raise RuntimeError(f'File not found: {fn}')

f = h5.File(fn, 'r')
grids = []
for g in f.keys():
    grids.append(g)
# First grid only
g = f[grids[0]]
names = []
fields = []
for k,v in g.items():
    fields.append(v[:])
    names.append(k)
f.close()

visible = np.zeros(len(fields), dtype='bool')
visible[0] = True
viewer = napari.Viewer(ndisplay=3)
print(names)
for i in range(len(fields)):
    viewer.add_image(fields[i], name=names[i], visible=visible[i])

if __name__ == '__main__':
    napari.run()
