"""
Bauhaus-Style Confusion Matrix Generator for A1 Poster
Creates a clean, geometric confusion matrix matching your poster aesthetic
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from matplotlib import rcParams


# Configure matplotlib for crisp, professional output
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Helvetica', 'Arial', 'DejaVu Sans']
rcParams['pdf.fonttype'] = 42  # TrueType fonts
rcParams['ps.fonttype'] = 42

def create_bauhaus_confusion_matrix(
    confusion_matrix,
    emotions,
    snr_level="5dB",
    accuracy=43,
    output_filename="confusion_matrix_bauhaus.png",
    colorscheme="grayscale"  # Options: "grayscale", "red_accent", "two_tone"
):
    """
    Create a Bauhaus-style confusion matrix
    
    Parameters:
    -----------
    confusion_matrix : 2D array
        The confusion matrix values (4x4 for 4 emotions)
    emotions : list
        List of emotion labels ['Angry', 'Calm', 'Happy', 'Sad']
    snr_level : str
        SNR level to display (e.g., "5dB")
    accuracy : float
        Overall accuracy percentage to display
    output_filename : str
        Output filename
    colorscheme : str
        Color scheme: "grayscale", "red_accent", or "two_tone"
    """
    
    # Create figure with specific size for A1 poster (12-14cm)
    # At 300 DPI: 12cm = 1417 pixels
    fig_width_inches = 5.5  # ~14cm at 300 DPI
    fig_height_inches = 5.5
    
    fig, ax = plt.subplots(figsize=(fig_width_inches, fig_height_inches), dpi=300)
    
    # Choose color scheme
    if colorscheme == "grayscale":
        # Pure grayscale gradient
        cmap = plt.cm.Greys
        vmin, vmax = 0, np.max(confusion_matrix)
    elif colorscheme == "red_accent":
        # White to red gradient (Bauhaus accent)
        cmap = plt.cm.Reds
        vmin, vmax = 0, np.max(confusion_matrix)
    elif colorscheme == "two_tone":
        # Black and white only
        cmap = plt.cm.binary_r
        vmin, vmax = 0, np.max(confusion_matrix)
    
    # Create the heatmap
    im = ax.imshow(confusion_matrix, cmap=cmap, aspect='equal', vmin=vmin, vmax=vmax)
    
    # Set ticks
    ax.set_xticks(np.arange(len(emotions)))
    ax.set_yticks(np.arange(len(emotions)))
    
    # Set tick labels - UPPERCASE for Bauhaus style
    ax.set_xticklabels(labels=emotions, fontsize=15, fontweight='bold')
    ax.set_yticklabels(labels=emotions, fontsize=15, fontweight='bold')
    
    # Rotate x labels for better fit
    plt.setp(ax.get_xticklabels(), rotation=0, ha="center")
    
    # Add axis labels
    ax.set_xlabel('Predicted emotion', fontsize=15, labelpad=15, style='italic')
    ax.set_ylabel('True emotion', fontsize=15, labelpad=15, style='italic')
    
    # Add text annotations with values
    for i in range(len(emotions)):
        for j in range(len(emotions)):
            value = confusion_matrix[i, j]
            
            # Choose text color based on cell brightness
            cell_color = im.cmap(im.norm(value))
            # Calculate perceived brightness
            brightness = (0.299 * cell_color[0] + 0.587 * cell_color[1] + 0.114 * cell_color[2])
            text_color = 'white' if brightness < 0.5 else 'black'
            
            # Add the value
            text = ax.text(j, i, int(value),
                          ha="center", va="center",
                          color=text_color, fontsize=28, fontweight='bold')
    
    # Add thick border around entire matrix (Bauhaus style)
 #   border_width = 1
 #   rect = mpatches.Rectangle((-0.5, -0.5), len(emotions), len(emotions),
 #                            fill=False, edgecolor='black', linewidth=border_width)
  #  ax.add_patch(rect)
    
    # Add gridlines between cells
  #  for i in range(len(emotions) + 1):
   #     ax.axhline(i - 0.5, color='black', linewidth=1)
  #      ax.axvline(i - 0.5, color='black', linewidth=1)
    
    # Remove spines
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    # Remove ticks
    ax.tick_params(which='both', length=0)
    
    # Tight layout
    plt.tight_layout()
    
    # Save with high quality
    plt.savefig(output_filename, dpi=300, bbox_inches='tight', 
                edgecolor='none', transparent=True)
    print(f"✓ Saved: {output_filename}")
    print(f"  Size: {fig_width_inches*300:.0f} x {fig_height_inches*300:.0f} pixels at 300 DPI")
    print(f"  Approximately 14cm × 14cm for A1 poster")
    
    return fig


def create_minimal_confusion_matrix(
    confusion_matrix,
    emotions,
    snr_level="5dB",
    output_filename="confusion_matrix_minimal.png"
):
    """
    Create an ultra-minimal confusion matrix (Morrison style)
    Even cleaner - just the essential information
    """
    
    fig_width_inches = 5.5
    fig_height_inches = 5.5
    
    fig, ax = plt.subplots(figsize=(fig_width_inches, fig_height_inches), dpi=300)
    
    # White to black only - no color
    cmap = plt.cm.Greys
    vmin, vmax = 0, np.max(confusion_matrix)
    
    # Create the heatmap
    im = ax.imshow(confusion_matrix, cmap=cmap, aspect='equal', vmin=vmin, vmax=vmax)
    
    # Minimal labels
    ax.set_xticks(np.arange(len(emotions)))
    ax.set_yticks(np.arange(len(emotions)))
    ax.set_xticklabels(fontsize=15, fontweight='bold')
    ax.set_yticklabels(fontsize=15, fontweight='bold')
    
    # Simple title
    ax.text(0.5, 1.08, f'{snr_level} SNR', transform=ax.transAxes, 
            fontsize=24, fontweight='bold', ha='center')
    
    # Add values
    for i in range(len(emotions)):
        for j in range(len(emotions)):
            value = confusion_matrix[i, j]
            cell_color = im.cmap(im.norm(value))
            brightness = (0.299 * cell_color[0] + 0.587 * cell_color[1] + 0.114 * cell_color[2])
            text_color = 'white' if brightness < 0.5 else 'black'
            
            ax.text(j, i, int(value), ha="center", va="center",
                   color=text_color, fontsize=26, fontweight='bold')
    
    # Thick border
    border_width = 4
    rect = mpatches.Rectangle((-0.5, -0.5), len(emotions), len(emotions),
                             fill=False, edgecolor='black', linewidth=border_width)
    ax.add_patch(rect)
    
    # Clean gridlines
    for i in range(len(emotions) + 1):
        ax.axhline(i - 0.5, color='black', linewidth=2)
        ax.axvline(i - 0.5, color='black', linewidth=2)
    
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    ax.tick_params(which='both', length=0)
    
    plt.tight_layout()
    plt.savefig(output_filename, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"✓ Saved: {output_filename}")
    
    return fig


# ============================================================================
# EXAMPLE USAGE - Replace with your actual 5dB data
# ============================================================================

if __name__ == "__main__":
    
    # Your 5dB confusion matrix data
    # Replace these numbers with your actual values!
    confusion_matrix_data = np.array([
        [12,  3,  4, 13],  # Angry predictions (True: Angry)
        [ 0, 31,  0, 1],  # Calm predictions (True: Calm)
        [ 0,  14,  6, 12],  # Happy predictions (True: Happy)
        [ 0, 26,  0, 6]   # Sad predictions (True: Sad)
    ])
    
    emotions = ['Angry', 'Calm', 'Happy', 'Sad']
    
    print("Creating Bauhaus-style confusion matrices...")
    print("=" * 60)
    
    # Version 1: Grayscale (classic Bauhaus)
    print("\n1. Grayscale version (recommended):")
    create_bauhaus_confusion_matrix(
        confusion_matrix_data,
        emotions,
        snr_level="5dB",
        accuracy=43,
        output_filename="confusion_matrix_grayscale.png",
        colorscheme="grayscale"
    )
    
    # Version 2: Red accent (more dramatic)
    print("\n2. Red accent version:")
    create_bauhaus_confusion_matrix(
        confusion_matrix_data,
        emotions,
        snr_level="5dB",
        accuracy=43,
        output_filename="confusion_matrix_red.png",
        colorscheme="red_accent"
    )
    
    # Version 3: Ultra minimal (Morrison style)
    print("\n3. Ultra-minimal version:")
    create_minimal_confusion_matrix(
        confusion_matrix_data,
        emotions,
        snr_level="5dB",
        output_filename="confusion_matrix_minimal.png"
    )
    
    print("\n" + "=" * 60)
    print("✓ Done! All versions created.")
    print("\nYou now have 3 options:")
    print("  1. confusion_matrix_grayscale.png - Classic Bauhaus")
    print("  2. confusion_matrix_red.png - With accent color")
    print("  3. confusion_matrix_minimal.png - Ultra-clean Morrison style")
    print("\nPick the one that matches your poster best!")
    print("\nAll are 300 DPI, ready to insert into PowerPoint.")