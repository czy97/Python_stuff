import matplotlib.pyplot as plt
import fire

def get_list(filePath):
    #each file line can only have one number
    data_list = []
    with open(filePath,'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            data_list.append(float(line))
    return data_list


def main(*args, savePath,skip = 1,title = 'Train loss'):
    '''
    :param args: multiple data file path
    :param savePath: the path to save the plot image
    '''

    for dataPath in args:
        label = dataPath.strip().split('/')[-1].split('.')[0]
        data_list = get_list(dataPath)
        data_index = list(range(1,len(data_list) + 1))

        plt.plot(data_index[::skip], data_list[::skip],'-o', label=label ,markersize=3)
        plt.legend(loc='best')

    plt.xlabel("epoch")
    plt.ylabel("loss")
    plt.title(title)

    plt.savefig(savePath,dpi=200)

if __name__ == '__main__':
    fire.Fire(main)
    
