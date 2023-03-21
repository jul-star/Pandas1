import pandas as pd


def f1(pickle_file: str):
    df = pd.read_pickle(pickle_file)
    small_df = df.iloc[49980:50019, :].copy()
    small_df.to_pickle('..\\input\\small_df.pickle')
    grouped = small_df.groupby('artist')
    print(type(grouped))
    for name, group_df in grouped:
        print('name=', name)
        print('\n', group_df)
        break


def f2():
    pickle_file = '..\\input\\small_df.pickle'
    small_df = pd.read_pickle(pickle_file)
    artist_grouped = small_df.groupby('artist')
    for name, group in artist_grouped:
        print(name, group['year'].min())


def f3():
    l = [1, 2, 3, 4, 5, 6, 7, None, 8, None, 10]
    s1 = pd.Series(l)
    mn = s1.min()
    print(s1[range(1, len(l), 3)])
    s1 = s1.fillna(mn)
    # print('\ns modified: \n', s1)


if __name__ == '__main__':
    # pickle_file = '..\\input\\df_artists.pickle'
    # f1(pickle_file)
    # f2()
    f3()
    print('\ndone')
