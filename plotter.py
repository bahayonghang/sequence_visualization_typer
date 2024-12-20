import numpy as np
import pathlib
import math

import matplotlib.pyplot as plt


font_name = "simhei"
plt.rcParams['font.family']= font_name # 指定字体，实际上相当于修改 matplotlibrc 文件　只不过这样做是暂时的　下次失效
plt.rcParams['axes.unicode_minus']=False # 正确显示负号，防止变成方框


def plot_npy(result_path: pathlib.Path) -> None:
    """
    plot true and prediction in npy format
    Args:
        result_path (pathlib.Path): path of result
    Examples:
        >>> plot_npy("result")
    """
    true_path = result_path.joinpath("true.npy")
    pred_path = result_path.joinpath("pred.npy")
    true_ndarray = np.load(true_path)
    pred_ndarray = np.load(pred_path)

    # 随机取一个length范围内的ndarray可视化
    length = true_ndarray.shape[0]
    random_index = np.random.randint(0, length)
    print(random_index)
    true = true_ndarray[random_index, :, -1]
    pred = pred_ndarray[random_index, :, -1]
    plt.figure(figsize=(20, 10), dpi=600)
    plt.plot(true, label='True')
    plt.plot(pred, label='Prediction')
    plt.legend()
    # plt.show()
    plt.savefig(result_path.joinpath("true_pred.png"), dpi=600)


def plot_npy_train(result_path: pathlib.Path) -> None:
    """
    plot true and prediction in npy format
    Args:
        result_path (pathlib.Path): path of result
    Examples:
        >>> plot_npy_train("result")
    """
    true_path = result_path.joinpath("true_train.npy")
    pred_path = result_path.joinpath("pred_train.npy")
    true_ndarray = np.load(true_path)
    pred_ndarray = np.load(pred_path)

    # 随机取一个length范围内的ndarray可视化
    length = true_ndarray.shape[0]
    random_index = np.random.randint(0, length)
    print(random_index)
    true = true_ndarray[random_index, :, -1]
    pred = pred_ndarray[random_index, :, -1]
    plt.figure(figsize=(20, 10), dpi=600)
    plt.plot(true, label='True')
    plt.plot(pred, label='Prediction')
    plt.legend()
    # plt.show()
    plt.savefig(result_path.joinpath("true_pred_train.png"), dpi=600)


def plot_npy_all(result_path: pathlib.Path) -> None:
    """
    plot all true and prediction in npy format
    Args:
        result_path (pathlib.Path): path of result
    Examples:
        >>> plot_npy_all("result")
    """
    true_path = result_path.joinpath("true.npy")
    pred_path = result_path.joinpath("pred.npy")
    true_ndarray = np.load(true_path)
    pred_ndarray = np.load(pred_path)

    print(f'true_ndarray shape: {true_ndarray.shape}')
    print(f'pred_ndarray shape: {pred_ndarray.shape}')

    # 如果存在name_list.txt，则读取name_list
    name_list_path = result_path.joinpath("name_list.txt")
    if name_list_path.exists():
        with open(name_list_path, 'r') as f:
            name_list = [line.strip() for line in f.readlines()]
    
    assert len(name_list) == true_ndarray.shape[2] == pred_ndarray.shape[2], "name_list的长度与true_ndarray和pred_ndarray的维度不一致"

    # 随机取一个length范围内的ndarray可视化
    length = true_ndarray.shape[0]
    random_index = np.random.randint(0, length)
    print(random_index)
    
    # 将指定索引的最后一个维度的所有数据可视化，并绘制在一张图中
    # 计算需要的行数和列数
    n_cols = min(3, true_ndarray.shape[2])  # 最多3列
    n_rows = math.ceil(true_ndarray.shape[2] / n_cols)

    # 创建一个自适应的子图网格
    fig, axs = plt.subplots(n_rows, n_cols, figsize=(4*n_cols, 3*n_rows))
    fig.suptitle('Visualization of test results for multi-dimensional data', fontsize=16)
    # 确保 axs 总是一个二维数组
    if true_ndarray.shape[2] == 1:
        axs = np.array([[axs]])
    elif n_rows == 1:
        axs = axs.reshape(1, -1)
    elif n_cols == 1:
        axs = axs.reshape(-1, 1)

    if name_list is not None:
        for i in range(true_ndarray.shape[2]):
            row = i // n_cols
            col = i % n_cols
            ax = axs[row, col]
            true = true_ndarray[random_index, :, i]
            pred = pred_ndarray[random_index, :, i]
            ax.plot(pred, label='Pred')
            ax.plot(true, label='True')
            ax.set_title(f'{name_list[i]}')
            ax.set_xlabel('Time steps')
            ax.set_ylabel('Values')
            ax.grid(True)
            ax.legend()
            print(f'True_{i} and Pred_{i} have been plotted')
    else:
        for i in range(true_ndarray.shape[2]):
            row = i // n_cols
            col = i % n_cols
            ax = axs[row, col]
            true = true_ndarray[random_index, :, i]
            pred = pred_ndarray[random_index, :, i]
            ax.plot(true, label='True')
            ax.plot(pred, label='Pred')
            ax.set_title(f'Dimension {i+1}')
            ax.set_xlabel('Time steps')
            ax.set_ylabel('Values')
            ax.grid(True)
            ax.legend()
            print(f'True_{i} and Pred_{i} have been plotted')

    # 移除多余的子图
    for i in range(true_ndarray.shape[2], n_rows * n_cols):
        row = i // n_cols
        col = i % n_cols
        fig.delaxes(axs[row, col])

    # 调整子图之间的间距
    plt.tight_layout()

    # 显示图形
    # plt.show()
    plt.savefig(result_path.joinpath("true_pred_all.png"), dpi=600)


def plot_npy_all_train(result_path: pathlib.Path) -> None:
    """
    plot all true and prediction in npy format
    Args:
        result_path (pathlib.Path): path of result
    Examples:
        >>> plot_npy_all_train("result")
    """
    true_path = result_path.joinpath("true_train.npy")
    pred_path = result_path.joinpath("pred_train.npy")
    true_ndarray = np.load(true_path)
    pred_ndarray = np.load(pred_path)

    print(f'true_ndarray shape: {true_ndarray.shape}')
    print(f'pred_ndarray shape: {pred_ndarray.shape}')

    # 如果存在name_list.txt，则读取name_list
    name_list_path = result_path.joinpath("name_list.txt")
    if name_list_path.exists():
        with open(name_list_path, 'r') as f:
            name_list = [line.strip() for line in f.readlines()]

    assert len(name_list) == true_ndarray.shape[2] == pred_ndarray.shape[2], "name_list的长度与true_ndarray和pred_ndarray的维度不一致"

    # 随机取一个length范围内的ndarray可视化
    length = true_ndarray.shape[0]
    random_index = np.random.randint(0, length)
    print(random_index)
    
    # 将指定索引的最后一个维度的所有数据可视化，并绘制在一张图中
    # 计算需要的行数和列数
    n_cols = min(3, true_ndarray.shape[2])  # 最多3列
    n_rows = math.ceil(true_ndarray.shape[2] / n_cols)

    # 创建一个自适应的子图网格
    fig, axs = plt.subplots(n_rows, n_cols, figsize=(4*n_cols, 3*n_rows))
    fig.suptitle('Visualization of test(train) results for multi-dimensional data', fontsize=16)
    # 确保 axs 总是一个二维数组
    if true_ndarray.shape[2] == 1:
        axs = np.array([[axs]])
    elif n_rows == 1:
        axs = axs.reshape(1, -1)
    elif n_cols == 1:
        axs = axs.reshape(-1, 1)

    if name_list is not None:
        for i in range(true_ndarray.shape[2]):
            row = i // n_cols
            col = i % n_cols
            ax = axs[row, col]
            true = true_ndarray[random_index, :, i]
            pred = pred_ndarray[random_index, :, i]
            ax.plot(pred, label='Pred')
            ax.plot(true, label='True')
            ax.set_title(f'{name_list[i]}')
            ax.set_xlabel('Time steps')
            ax.set_ylabel('Values')
            ax.grid(True)
            ax.legend()
            print(f'True_{i} and Pred_{i} have been plotted')
    else:
        for i in range(true_ndarray.shape[2]):
            row = i // n_cols
            col = i % n_cols
            ax = axs[row, col]
            true = true_ndarray[random_index, :, i]
            pred = pred_ndarray[random_index, :, i]
            ax.plot(true, label='True')
            ax.plot(pred, label='Pred')
            ax.set_title(f'Dimension {i+1}')
            ax.set_xlabel('Time steps')
            ax.set_ylabel('Values')
            ax.grid(True)
            ax.legend()
            print(f'True_{i} and Pred_{i} have been plotted')

    # 移除多余的子图
    for i in range(true_ndarray.shape[2], n_rows * n_cols):
        row = i // n_cols
        col = i % n_cols
        fig.delaxes(axs[row, col])

    # 调整子图之间的间距
    plt.tight_layout()

    # 显示图形
    # plt.show()
    plt.savefig(result_path.joinpath("true_pred_all_train.png"), dpi=600)
