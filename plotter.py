import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

def plotme(data, data_type):
    fig, ax = plt.subplots()

    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')

    method_name = 'Experimental method' if data_type == 1 else 'Numerical method'
    ax.plot(data[0][0], data[1][0], marker='o', markersize=3, color='r', label=method_name)
    plt.grid(linestyle='--', linewidth=0.5)

    plt.legend(bbox_to_anchor=(1.05, 1.04), shadow=True)

    ax.set_xlabel(data[0][1], labelpad=10)
    ax.set_ylabel(data[1][1], labelpad=10)
    ax.xaxis.set_label_coords(0.5, -0.025)

    plt.show()
    plt.tight_layout()
    fig.savefig(f'polars/{method_name.replace(" ","-").lower()}-polar-{data[0][2]}-{data[1][2]}' + '.png', dpi=1000, bbox_inches='tight')


def plotus(edata, ndata):
    fig, ax = plt.subplots()

    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')

    ax.plot(edata[0][0], edata[1][0], marker='o', markersize=3, color='r', label='Experimental method')
    ax.plot(ndata[0][0],ndata[1][0],marker='x',markersize=3,color='b',label='Numerical method')
    plt.grid(linestyle='--', linewidth=0.5)

    plt.legend(bbox_to_anchor=(1.05, 1.04), shadow=True)

    ax.set_xlabel(edata[0][1], labelpad=10)
    ax.set_ylabel(edata[1][1], labelpad=10)
    ax.xaxis.set_label_coords(0.5, -0.025)

    plt.show()
    plt.tight_layout()
    fig.savefig(f'polars/combined-polar-{edata[0][2]}-{edata[1][2]}' + '.png', dpi=1000, bbox_inches='tight')
