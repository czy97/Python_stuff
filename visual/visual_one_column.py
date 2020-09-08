#!/mnt/lustre/sjtu/home/czy97/.conda/envs/pytorch1_6/bin/python
import matplotlib.pyplot as plt
import fire


def main(log_path, save_path, data_loc=0, skip=1):

    data = []
    with open(log_path, 'r') as f:
        for line in f.readlines():
            data.append(float(line.strip().split()[data_loc]))

    data_index = list(range(1, len(data) + 1))
    plt.plot(data_index[::skip], data[::skip], '-o', markersize=3)
    plt.savefig(save_path, dpi=200)


if __name__ == '__main__':
    fire.Fire(main)

