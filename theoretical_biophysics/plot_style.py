import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault

def apply_my_plot_style_globally():
    plt.rcParams.update({
        'figure.dpi': 200,
        'font.family': 'sans-serif',
        'font.sans-serif': 'DejaVu Sans',  # Fast rendering and close to Computer Modern Sans Serif
        'font.size': 12,  # For figure captions
        'axes.titlesize': 10,  # Titles in figures (e.g., A., B., ...)
        'axes.labelsize': 10,  # Axis labels
        'xtick.labelsize': 8,  # Tick labels on x-axis
        'ytick.labelsize': 8,  # Tick labels on y-axis
        'legend.fontsize': 8,  # Legends and data labels
        'legend.title_fontsize': 10,
        'savefig.format': 'eps',  # Save figures as EPS by default
        'savefig.dpi': 200,
        'text.usetex': True,
        'lines.linewidth': 0.5,
        'lines.markersize'  : 3.0,
        'axes.prop_cycle': plt.cycler('color', plt.cm.Set1.colors)
    })
    
def set_one_column_figure(width_mm=90, aspect_ratio=1.618):
    width_inch = width_mm / 25.4  # Convert width to inches
    height_inch = width_inch / aspect_ratio  # Calculate height based on aspect ratio
    plt.figure(figsize=(width_inch, height_inch))
    print(f'for latex figure: width={width_mm}mm, height={round(width_mm/aspect_ratio, 2)}mm')

def set_two_column_figure(width_mm=180, aspect_ratio=1.618):
    width_inch = width_mm / 25.4  # Convert width to inches
    height_inch = width_inch / aspect_ratio  # Calculate height based on aspect ratio
    plt.figure(figsize=(width_inch, height_inch))
    print(f'for latex figure: width={width_mm}mm, height={round(width_mm/aspect_ratio, 2)}mm')
    
def set_full_page_figure(width_mm=180, aspect_ratio=1.618):
    width_inch = width_mm / 25.4  # Convert width to inches
    height_inch = width_inch / aspect_ratio  # Calculate height based on aspect ratio
    plt.figure(figsize=(width_inch, height_inch))
    print(f'for latex figure: width={width_mm}mm, height={round(width_mm/aspect_ratio, 2)}mm')