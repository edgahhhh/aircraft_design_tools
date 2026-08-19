""" plt 
module with some functions to make plotting easier
"""
import matplotlib.pyplot as plt

def plt_2d_subplot(x,y,nrows, ncols, index,
                   title,xlabel,ylabel):
    """ plot 3d figure in a subplot 
    
    - create a figure before calling function
    """
    f=plt.gcf()
    ax=f.add_subplot(nrows,ncols,index)
    ax.set_title(title)
    ax.plot(x,y)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return ax


def plt_3d(x,y,z,title,xlabel,ylabel,zlabel,
           c=None, clabel=None):
    """ plot 3d points """
    plt.figure()
    ax=plt.gcf().add_subplot(111,projection='3d')
    ax.set_title(title)
    if c is None:
        sc=ax.scatter(x,y,z)
    else:
        sc=ax.scatter(x,y,z,c=c,cmap='magma')
        cb=plt.gcf().colorbar(sc, ax=ax, pad=0.1)
        if clabel is None:
            # set to zlabel if not given
            cb.set_label(zlabel)
        else:
            cb.set_label(clabel)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    return sc

def plt_bars(labels, values, nrows, ncols, index,
             title, ylabel):
    """ plot a bar chart with labels and values
    
    - create a figure before calling function
    - labels must be label type
    """
    f=plt.gcf()
    ax=f.add_subplot(nrows, ncols, index)
    ax.set_title(title)
    ax.bar(labels, values)
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_ylabel(ylabel)
