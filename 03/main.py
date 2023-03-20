import pandas as pd


def f1():
    df = pd.read_csv('..\\input\\artwork_data.csv', nrows=5)
    print('df \n', df)
    print('df.column: \n', df.columns)


def f2():
    cols_to_use = ['id',  'artist',  'title',
                   'medium', 'year', 'acquisitionYear',
                   'width', 'height', 'units']
    df = pd.read_csv('..\\input\\artwork_data.csv', nrows=5,
                     index_col='id', usecols=cols_to_use)
    print('df \n', df)
    print('df.column: \n', df.columns)


def f3():
    cols_to_use = ['id',  'artist',  'title',
                   'medium', 'year', 'acquisitionYear',
                   'width', 'height', 'units']
    df = pd.read_csv('..\\input\\artwork_data.csv',
                     index_col='id', usecols=cols_to_use)
    df.to_pickle('data_frame.pickle')


if __name__ == '__main__':
    f3()
