import pandas as pd


def f1(pickle_file: str):
    df = pd.read_pickle(pickle_file)
    print('records: ', len(df))
    index_key = df.keys()[0]
    print('index key: ', index_key)
    print('records by key: ', len(df[index_key]))
    print('records as ids: ', len(df.index))


def f2(pickle_file: str):
    df = pd.read_pickle(pickle_file)
    if 'artist' in df.columns:
        artists = df['artist']
        ar = pd.unique(artists)
        print('unique artists number is ', len(ar))
    else:
        print('There is no artist column')


def f3(pickle_file: str):
    df = pd.read_pickle(pickle_file)
    if 'artist' in df.columns:
        s = df['artist'] == 'Bacon, Francis'
        print('Bacons art works: ', s.value_counts())
    else:
        print('There is no artist column')


def f4(pickle_file: str):
    df = pd.read_pickle(pickle_file)
    if 'artist' in df.columns:
        # print(df['artist'][:5])
        # s = df.loc[df['artist'].str.contains('Julian'), :]
        s = df['artist'].str.contains('Julian')
        print('Julian art works: ', s.value_counts())
    else:
        print('There is no artist column')


def f5(pickle_file: str):
    df = pd.read_pickle(pickle_file)
    print(df.iloc[1:5, [3, 5, 7]])


def f6(pickle_file: str):
    df = pd.read_pickle(pickle_file)
    df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')
    df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')
    df.loc[:, 'area'] = df.loc[:, 'width']*df.loc[:, 'height']
    mx = max(df['area'])
    print(len(df.index), '\n',
          df.loc[df['area'] < 500, :])


if __name__ == '__main__':
    file_path = '..\\input\\df_artists.pickle'
    f6(file_path)
    print('\ndone')
