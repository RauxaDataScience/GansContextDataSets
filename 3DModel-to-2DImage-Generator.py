#pip install numpy-stl

from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

stl_mesh = mesh.Mesh.from_file('./chair.stl')

def generate_save_figure(elev,azim,dist):         
    figure = pyplot.figure(figsize=(1,1))
    axes = mplot3d.Axes3D(figure)
    axes.grid(False)
    axes._axis3don=False    
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(stl_mesh.vectors))
    scale = stl_mesh.points.flatten(-1)
    axes.auto_scale_xyz(scale, scale, scale)
    axes.view_init(elev=elev,azim=azim)
    axes.dist = dist
    axes.autoscale(True)
    figure.savefig('./images/elev({})-azim({})-dist({}).png'.format(elev,azim,dist))   
    print('saved elev {}, azim {}, dist {}'.format(elev,azim,dist))
    del figure,axes,scale
    pyplot.close('all')

for elev in range(0,180,1):
    for azim in range(0,360,1):
        for dist in range(5,25,1):
            generate_save_figure(elev,azim,dist)
                