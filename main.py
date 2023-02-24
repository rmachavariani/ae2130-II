import numpy as np
import io
from plotter import plotme, plotus


def ask_for_input():
    options = ['2D', '3D', 'combined']
    answer = ''
    question = "Which data type should I visualize?\n"

    for key, option in enumerate(options):
        question += f'{key + 1}. {option}\n'

    question += 'Choice: '

    while answer not in map(str, range(1, len(options) + 1)):
        answer = input(question)

    print('You picked: ' + options[int(answer) - 1])

    return int(answer)

def select_and_plot(data_type):
    experimental_data = get_experimental_data()
    numerical_data = get_numerical_data()

    alpha_e = [experimental_data[:, 1].astype(float), r"$\alpha$ [$\degree$]", "alpha"]
    c_lift_e = [experimental_data[:, 3].astype(float), "$C_{L}$", "cl"]
    c_drag_e = [experimental_data[:, 4].astype(float), "$C_{D}$", "cd"]
    c_moment_e = [experimental_data[:, 11].astype(float), "$C_{M}$", "cm"]

    alpha_n = [numerical_data[:, 0].astype(float), r"$\alpha$[$\degree$]", "alpha"]
    c_lift_n = [numerical_data[:, 2].astype(float), "$C_{L}$", "cl"]
    c_drag_n = [numerical_data[:, 5].astype(float), "$C_{D}$", "cd"]
    c_moment_n = [numerical_data[:, 8].astype(float), "$C_{M}$", "cm"]

    if data_type == 1:
        plotme([alpha_e,c_lift_e], data_type)
        plotme([alpha_e,c_moment_e], data_type)
        plotme([alpha_e, c_drag_e], data_type)
        plotme([c_drag_e,c_lift_e], data_type)

    elif data_type == 2:
        plotme([alpha_n, c_lift_n], data_type)
        plotme([c_drag_n,c_lift_n], data_type)
        plotme([alpha_n,c_moment_n], data_type)
        plotme([alpha_n, c_drag_n], data_type)

    elif data_type == 3:
        plotus([alpha_e, c_lift_e], [alpha_n, c_lift_n])
        plotus([alpha_e, c_moment_e], [alpha_n,c_moment_n])
        plotus([alpha_e, c_drag_e], [alpha_n, c_drag_n])
        plotus([c_drag_e, c_lift_e], [c_drag_n,c_lift_n])

    else:
        print("Data type requested can not be analyzed")


def get_experimental_data():
    experimental_data = []
    with io.open('data/2dnumericaldata.txt', mode="r", encoding="utf-8") as f:
        next(f)
        next(f)
        for line in f:
            experimental_data.append(line.split())

    return np.array(experimental_data)

def get_numerical_data():
    numerical_data = []
    with io.open('data/3dnumericaldata.txt', mode="r", encoding="utf-8") as f:
        for i in range(1, 9):
            next(f)

        for line in f:
            numerical_data.append(line.split())

    return np.array(numerical_data[0::10])


if __name__ == '__main__':
    # ask which data type user wants to visualize
    data_type = ask_for_input()
    # visualize
    select_and_plot(data_type)
