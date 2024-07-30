# PhD Thesis in Theoretical Biophysics

Welcome to the repository supporting my PhD thesis in Theoretical Biophysics. This repository is organized into various folders containing Jupyter Notebooks 
that illustrate key concepts of Biology Physics discussed in my thesis, a few basic methods of Bioimage Analysis, Statistical Methods often used in biology and a short revision os Statistical Physics Basics. 
Below is an overview of the structure and content of the repository.


## Repository Structure

- `diffusion_equation/`
  - `1_solving_diffusion_equation.ipynb` This notebook demonstrates the analytical and numerical solutions of the simplest case of the diffusion equation in a 1D system.
  - `2_diffusion_degradation_production.ipynb` Here, constant production and degradation are added to the diffusion dynamics - numerically simulated dynamics relax to a steady state.
  - `3_boundary_conditions.ipynb` Reflecting and absorbing boundaries influence diffusion dynamics and can be implemented both numerically and analytically. 
    
- `pattern_formation_examples/`
  - `french_flag_model.ipynb`
  - `turing_patterns.ipynb`
    
- `statistical_physics_basics/`
  - `statistical_physics.ipynb` (Example on the Ising model or Boltzmann distribution)
  - `nonlinear_dynamics.ipynb` (Chaos theory and logistic map)
  - `brownian_motion.ipynb` (Simulation of Brownian motion and its properties)

- `image_analysis/`
  - `segmentation_by_thresholding.ipynb` (Comparison of Otsu's method and adaptive thresholding, and simple ML algorithms like k-means clustering and a basic neural network)
  - `filtering_1d_basic.ipynb` (Standard filtering techniques for 1D signals)
  - `working_with_surfaces.ipynb` (Definitions and basic operations: surfaces, transformation matrices, etc.)

- `statistics/`
  - `regression_fitting.ipynb` (Fitting regression models, defining p-value)
  - `statistical_tests.ipynb` (Conducting statistical tests to determine changes in data)
  - `bayesian_statistics.ipynb` (Introduction to Bayesian inference and its applications)
  - `markov_chains.ipynb` (Introduction to Markov chains and their applications)


## Acknowledgements

I would like to thank my advisor Prof. Benjamin M Friedrich and his group "Biological Algorithms" in TU Dresden.
