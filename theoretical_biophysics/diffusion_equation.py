import numpy as np

def analytical_solution(x, t, D, N):
    """
    Analytical solution of diffusion equation \partial_{t} c(x, t) = D \partial_{x}^{2} c(x, t).
    explained in example_notebooks/diffusion_equation/1_solving_diffusion_equation
    Parameters:
    x  : np.array
    t  : float   - time point
    D  : float   - diffusion coefficient
    N  : int     - number of particles
    Returns:
    np.array
    """
    return (N / np.sqrt(4 * np.pi * D * t)) * np.exp(-x**2 / (4 * D * t))

def numerical_laplacian(c, dx):
    """
    Numerical lapplacian for the concentration array.
    explained in example_notebooks/diffusion_equation/1_solving_diffusion_equation
    Parameters:
    c  : np.array - concentration array
    dx : float   - spatial discretization size
    Returns:
    np.array
    """
    c_iminus  = np.roll(c, 1)
    c_iplus   = np.roll(c, -1)
    laplacian = (c_iplus - 2*c + c_iminus)/dx**2
    return laplacian

def chi(x, w):
    """
    Shape function of particles production region.
    explained in example_notebooks/diffusion_equation/2_diffusion_degradation_production
    Parameters:
    x  : np.array - spatial coordinates
    w  : float   - size of production region centered at x = 0
    Returns:
    np.array
    """
    return (x <= w/2) * (x >= -w/2) * 1/w

def chi_x0(x, w, x0):
    """
    Shape function of the particles' production region: a rectangular production region 
    starting at position x0 with width w.
    Parameters:
    x  : np.array - spatial coordinates
    w  : float   - size of production region centered at x = 0
    Returns:
    np.array
    """
    return (x >= x0) * (x <= x0 + w) * 1/w

def G(x, D, beta):
    """
    Green's function of operator D d^2 - beta
    explained in example_notebooks/diffusion_equation/2_diffusion_degradation_production
    Parameters:
    x   :  np.array - spatial coordinates
    D   :  float - diffusion coefficient 
    beta:  float - degradation rate
    Returns:
    np.array
    """
    lam = np.sqrt(D/beta)
    return np.exp(-np.abs(x)/lam)/np.sqrt(D*beta)/2

def steady(x, D, beta, alpha, w, dx):
    """
    Steady state of diffusion equation found as the convolution of its operator Green's function and production term.
    explained in example_notebooks/diffusion_equation/2_diffusion_degradation_production
    Parameters:
    x    :  np.array - spatial coordinates
    D    :  float - diffusion coefficient 
    beta :  float - degradation rate
    alpha:  float - production rate
    w    :  float - production region width
    dx   : float   - spatial discretization size
    Returns:
    np.array
    """
    return np.convolve(G(x, D, beta), alpha * chi(x, w), mode='same') * dx

def steady_x0(x, D, beta, alpha, w, x0, dx):
    """
    Steady state of diffusion equation found as the convolution of its operator Green's function and production term.
    The production source at position x0.
    Parameters:
    x    :  np.array - spatial coordinates
    D    :  float - diffusion coefficient 
    beta :  float - degradation rate
    alpha:  float - production rate
    w    :  float - production region width
    dx   : float   - spatial discretization size
    Returns:
    np.array
    """
    return np.convolve(G(x, D, beta), alpha * chi_x0(x, w, x0), mode='same') * dx

def euler_scheme(dx, Lmax, dt, ndt, D, beta, alpha, w, boundary=None):
    """
    Function to find numerically the solution of diffisuon equation with different boundary conditions using Euler scheme.
    Boundary conditions are introduced in example_notebooks/diffusion_equation/3_boundary_conditions
    Parameters:
    dx      :  float - spatial bin size
    Lmax    :  float - system size
    dt      :  float - temporal bin size
    ndt     :  int   - numver of time steps
    D       :  float - diffusion coefficient 
    beta    :  float - degradation rate
    alpha   :  float - production rate
    w       :  float - production region widthc
    boundary:  str   - boundary conditions, by default None, 'reflect' or 'absorb'
    Returns:
    ct : list - concentration profiles at different time points
    """
    
    # additional bins to implement reflecting boundary conditions
    if boundary==None:
        Lmax = Lmax * 20 # system size, boundaries are far away ~ infinity
        
    x   = np.linspace(-Lmax-dx, Lmax+dx, 2*int(Lmax/dx)+1+2)
    ndx = len(x)

    # list for the spatial profiles of concentration c as function of time
    ct = []

    # inital conditions: zero concentration profile
    c0 = np.zeros_like(x)
    ct.append(c0)

    # loop through time 
    for n in tqdm( range(1, ndt) ):
        c_n = ct[-1]   
        c_nplus = c_n + (D * numerical_laplacian(c_n, dx) - beta * c_n + alpha * chi(x, w)) * dt
        if boundary==None:
            ct.append(c_nplus)
        elif boundary=='period':
            ct.append(c_nplus)
        elif boundary=='reflect':
            # 'returning' the concentration 'leaked' to the additional bins
            c_nplus[1]  = c_nplus[1] + c_nplus[0]
            c_nplus[-2] = c_nplus[-2] + c_nplus[-1]
            c_nplus[0]  = c_nplus[-1] = 0
            ct.append(c_nplus)
        elif boundary=='absorb':
            # 'absorb' the concentration 'leaked' to the additional bins
            c_nplus[0]  = c_nplus[-1] = c_nplus[1] = c_nplus[-2] = 0
            ct.append(c_nplus)
    # removing additional bins
    ct = [cn[1:-1 ]for cn in ct]
    
    return x[1:-1], ct