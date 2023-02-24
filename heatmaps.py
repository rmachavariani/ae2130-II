import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib

matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'


# Visualize heat distribution per each angle of attack of a 2D wing
def heatmap(df, aoa, direction):
    df = df.iloc[:, 150:450]
    aoa_value = aoa.split('a', 1)[1].replace("b", "")

    z = df.values
    fig, ax = plt.subplots()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(r'$\alpha$ = ' + aoa_value + r'$\degree$ ' + direction)
    loc = matplotlib.ticker.MultipleLocator(base=25.0)
    ax.xaxis.set_major_locator(loc)
    plt.xticks(rotation=45, ha='left')
    plt.grid(linestyle='--', linewidth=0.5)

    c = ax.imshow(z, cmap=cm.coolwarm, interpolation="bicubic")
    cbar = fig.colorbar(c, ax=ax)
    cbar.ax.get_yaxis().labelpad = 15
    cbar.ax.set_ylabel(r'T [C$\degree$]', rotation=270)

    fig.savefig('heatmaps/heatmap-' + direction + '-' + aoa_value + '.png', dpi=700)
    plt.tight_layout()

    #plt.show()


if __name__ == '__main__':
    aoa_directions = {'increasing': 'temperature_data/forward', 'decreasing': 'temperature_data/reverse'}
    for aoa_direction, directory in aoa_directions.items():
        child_dirs = [f for f in os.listdir(directory) if not f.startswith('.')]
        for child_directory in child_dirs:
            aoa_directory = os.path.join(directory, child_directory)
            aoa_value = os.path.basename(aoa_directory)
            thermo_files = [f for f in os.listdir(aoa_directory) if os.path.isfile(os.path.join(aoa_directory, f))]
            if len(thermo_files) > 1:
                thermo_data = pd.read_csv(os.path.join(aoa_directory, thermo_files[4]), header=None, delimiter=';')
                heatmap(thermo_data, aoa_value, aoa_direction)
