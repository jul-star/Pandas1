import pandas as pd


def f1(pickle_file: str):
    df = pd.read_pickle(pickle_file)
    small_df = df.iloc[49980:50019, :].copy()
    grouped = small_df.groupby('artist')
    print(type(grouped))
    for name, group_df in grouped:
        print('name=', name)
        print('\n', group_df)


if __name__ == '__main__':
    pickle_file = '..\\input\\df_artists.pickle'
    f1(pickle_file)
    print('\ndone')
