import matplotlib.pyplot as plt
import numpy as np
import sys

figure_folder = 'figure'
raw_data_folder = 'raw_data'


def draw_ac_rate_safe_unsafe_cdf():
    raw_data = np.genfromtxt(f'{raw_data_folder}/single_safe_paper_result.csv', delimiter=',')

    ic3_ac_rate = raw_data[1:, 7]
    fsis_ac_rate = raw_data[1:, 11]
    i234_ac_rate = raw_data[1:, 20]
    print(ic3_ac_rate)
    print(fsis_ac_rate)
    print(i234_ac_rate)

    def count_1(A):
        cnt = 0
        for a in A:
            if a > 0.99:
                cnt += 1
        return cnt

    print(f'IC3 {count_1(ic3_ac_rate)}')
    print(f'FSIS {count_1(fsis_ac_rate)}')
    print(f'i234 {count_1(i234_ac_rate)}')

    data_list = [i234_ac_rate, ic3_ac_rate, fsis_ac_rate]
    legend_list = ['INCISE', 'IC3', 'FSIS']

    font = {'family': 'sans-serif',
            'weight': 'normal',
            'size': 14}

    plt.rc('font', **font)
    fig = plt.figure(figsize=(8, 3.2))
    ax2 = fig.add_subplot(121)
    ax2.set_xlabel('$Coverage$')
    ax2.set_ylabel('$p$')
    ax2.set_title('(a)')

    for i, alg in enumerate(data_list):
        alg_inv = [1.0 - _point for _point in alg]

        data = alg_inv
        data_sorted = np.sort(data)

        p = 1. * np.arange(len(data)) / (len(data) - 1)
        p_inv = [1.0 - i for i in p]

        ax2.plot(data_sorted, p, label=legend_list[i])
        labels = ['1.0', '0.8', '0.6', '0.4', '0.2', '0.0']
        plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], labels)
        ax2.grid(ls='--')

    ax2.legend(loc='lower right')
    ax2.set_ylim(ymin=0, ymax=1)

    raw_data_2 = np.genfromtxt(f'{raw_data_folder}/single_unsafe_paper_result.csv', delimiter=',')

    i234_ac_rate_2 = raw_data_2[1:, 12]

    print(i234_ac_rate_2)

    data_list_2 = [i234_ac_rate_2]
    legend_list_2 = ['INCISE']

    ax2_2 = fig.add_subplot(122)

    ax2_2.set_xlabel('$Coverage$')

    ax2_2.set_title('(b)')

    for i, alg in enumerate(data_list_2):
        alg_inv_2 = [1.0 - _point for _point in alg]

        data_2 = alg_inv_2
        data_sorted_2 = np.sort(data_2)
        p_2 = 1. * np.arange(len(data_2)) / (len(data_2) - 1)
        p_inv_2 = [1.0 - i for i in p_2]

        ax2_2.plot(data_sorted_2, p_2, label=legend_list_2[i])
        labels = ['1.0', '0.8', '0.6', '0.4', '0.2', '0.0']
        plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], labels)
        ax2_2.grid(ls='--')

    ax2_2.set_ylim(ymin=0, ymax=1)
    ax2_2.legend(loc='lower right')

    plt.tight_layout(pad=0.3, w_pad=1)
    plt.savefig(f"{figure_folder}/fig3_ac_rate_single_safe_unsafe.pdf")
    plt.show()


def draw_runtime_safe_unsafe_cdf():
    raw_data = np.genfromtxt(f'{raw_data_folder}/single_safe_paper_result.csv', delimiter=',')

    ic3_ac_rate = raw_data[1:, 9]
    fsis_ac_rate = raw_data[1:, 13]
    i234_ac_rate = raw_data[1:, 17]
    print(ic3_ac_rate)
    print(fsis_ac_rate)
    print(i234_ac_rate)

    data_list = [i234_ac_rate, ic3_ac_rate, fsis_ac_rate]
    legend_list = ['INCISE', 'IC3', 'FSIS']

    font = {'family': 'sans-serif',
            'weight': 'normal',
            'size': 14}

    plt.rc('font', **font)
    fig = plt.figure(figsize=(8, 3.2))

    ax2 = fig.add_subplot(121)
    plt.xscale("log")
    ax2.set_xlabel('$Time\ (s)$')
    ax2.set_ylabel('$p$')
    ax2.set_title('(a)')

    for i, alg in enumerate(data_list):
        data = alg

        data_sorted = np.sort(data)

        p = 1. * np.arange(len(data)) / (len(data) - 1)
        p_inv = [1.0 - i for i in p]

        ax2.semilogx(data_sorted, p, label=legend_list[i])
        ax2.grid(ls='--')

    plt.legend(loc='lower right')
    ax2.set_ylim(ymin=0, ymax=1)

    raw_data_2 = np.genfromtxt(f'{raw_data_folder}/single_unsafe_paper_result.csv', delimiter=',')

    i234_ac_rate_2 = raw_data_2[1:, 9]

    print(i234_ac_rate_2)

    data_list_2 = [i234_ac_rate_2]
    legend_list_2 = ['INCISE']

    ax2_2 = fig.add_subplot(122)
    plt.xscale("log")
    ax2_2.set_xlabel('$Time\ (s)$')

    ax2_2.set_title('(b)')

    for i, alg in enumerate(data_list_2):
        data_2 = alg

        data_sorted_2 = np.sort(data_2)

        p_2 = 1. * np.arange(len(data_2)) / (len(data_2) - 1)
        p_inv_2 = [1.0 - i for i in p_2]

        ax2_2.plot(data_sorted_2, p_2, label=legend_list_2[i])
        ax2_2.grid(ls='--')
    plt.legend(loc='lower right')
    ax2_2.set_ylim(ymin=0, ymax=1)

    plt.tight_layout(pad=0.3, w_pad=1)
    plt.savefig(f"{figure_folder}/fig4_runtime_single_safe_unsafe.pdf")
    plt.show()


def draw_random_ac_rate_safe_lmcs_cu():
    raw_data = np.genfromtxt(f'{raw_data_folder}/live_safe_variable_k_paper_result.csv', delimiter=',', dtype=None)

    aig_name_list_raw = raw_data[1:, 0]
    aig_name_list = []
    for aig_name_raw in aig_name_list_raw:
        aig_name, _ = str(aig_name_raw.decode()).split('_')
        if aig_name not in aig_name_list:
            aig_name_list.append(aig_name)

    random_ac_rate_dict = {}
    for aig_name in aig_name_list:
        random_ac_rate_dict[aig_name] = []

    for line in raw_data[1:]:
        aig_name = (line[0].decode()).split('_')[0]
        random_ac_rate_dict[aig_name].append(float(line[13].decode()))

    aig_name_list = [aig_name for aig_name in aig_name_list if
                     not aig_name.endswith('ro.aig') and not aig_name.startswith('lmcs06')]

    data_list = [random_ac_rate_dict[aig_name] for aig_name in aig_name_list]
    legend_list = aig_name_list

    font = {'family': 'sans-serif',
            'weight': 'normal',
            'size': 14}

    plt.rc('font', **font)
    fig = plt.figure(figsize=(8, 3.2))
    ax2 = fig.add_subplot(121)
    ax2.set_xlabel('$\#\ Trials$')
    ax2.set_xticks(range(0, 50 + 1, 10))

    ax2.set_ylabel('$AC\ Ratio$')
    ax2.set_yticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax2.set_ylim(ymin=0.5, ymax=1.04)
    ax2.set_title('(a)')

    for i, alg in enumerate(data_list):
        data = alg

        ax2.plot(data, label=legend_list[i])
        ax2.grid(ls='--')

    raw_data = np.genfromtxt(f'{raw_data_folder}/live_safe_variable_k_paper_result.csv',
                             delimiter=',', dtype=None)

    aig_name_list_raw = raw_data[1:, 0]
    aig_name_list = []
    for aig_name_raw in aig_name_list_raw:
        aig_name, _ = str(aig_name_raw.decode()).split('_')
        if aig_name not in aig_name_list:
            aig_name_list.append(aig_name)

    random_ac_rate_dict = {}
    for aig_name in aig_name_list:
        random_ac_rate_dict[aig_name] = []

    for line in raw_data[1:]:
        aig_name = (line[0].decode()).split('_')[0]
        random_ac_rate_dict[aig_name].append(float(line[13].decode()))

    aig_name_list_2 = [aig_name for aig_name in aig_name_list if
                       not aig_name.endswith('ro.aig') and not aig_name.startswith('cu')]

    data_list_2 = [random_ac_rate_dict[aig_name] for aig_name in aig_name_list_2]
    legend_list_2 = aig_name_list_2

    ax2_2 = fig.add_subplot(122)
    ax2_2.set_xlabel('$\#\ Trials$')
    ax2_2.set_yticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax2_2.set_xticks(range(0, 50 + 1, 10))
    ax2_2.set_ylim(ymin=0.5, ymax=1.04)
    ax2_2.set_title('(b)')

    for i, alg in enumerate(data_list_2):
        data = alg

        ax2_2.plot(data, label=legend_list_2[i])
        ax2_2.grid(ls='--')

    plt.tight_layout(pad=0.3, w_pad=1)
    plt.savefig(f"{figure_folder}/fig5_live_variable_k_safe_lmcs_cu.pdf")
    plt.show()


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'fig3':
        draw_ac_rate_safe_unsafe_cdf()
    elif cmd == 'fig4':
        draw_runtime_safe_unsafe_cdf()
    elif cmd == 'fig5':
        draw_random_ac_rate_safe_lmcs_cu()
    else:
        print("python paper_figure_generator fig3|fig4|fig5")
