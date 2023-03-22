import pandas as pd
import numpy as np
from random import randint, choice, shuffle
from faker import Faker


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


def f4():
    l = np.random.rand(10)
    s1 = pd.Series(l)
    print(type(s1))
    s2 = s1 + 1
    # print('S2: \n', s2)
    print(s1[s1 > 0.5])
    print('max=', s1.max(), ', min=', s1.min(), ', ', s1.count())
    print(s1.describe())


def f5():
    l = ['a', 'b', 'c']
    n = [1, -3, 5]
    sl = pd.Series(l, name='letters')
    sn = pd.Series(n, name='int')
    s = pd.Series(l, index=n, name='letters')

    # print(sl.values, sl.name, sl[1])
    print(s.name, ': ', s.transpose())
    print('product of ', sn.name, ': ', sn.product())


def f6():
    sl = pd.Series(np.random.rand(100), name='random')
    # print(sl.head(-10))
    print(sl.take([1, 10, 30, 50]))


def f7():
    s = pd.Series(np.random.rand(100)*100+10)
    print(s.tail(5))
    print('3-9: \n', s[3:9])
    print('9-3: \n', s[9:3:-1])


def f8():
    idx = [choice([0, 1, 2, 3]) for i in range(10)]
    non_unique = pd.Series(np.random.rand(10)*100 % 100, index=idx)
    print(non_unique.to_list())
    # l - label
    l = 1
    print('iloc: ', l, non_unique.iloc[l])
    print('loc: ', l, ': ', non_unique.loc[l].index, '~', non_unique.loc[l])


def f9():
    s = pd.Series(np.random.rand(15)*100 % 10)
    s_sorted = s.sort_values()
    s_2 = s.sort_values(ascending=False)
    fake = Faker()
    l = [fake.name() for i in range(10)]
    s_l = pd.Series(l, name='Faked names')
    s_l.sort_values(inplace=True)
    print(s.to_list())
    print(s_sorted.to_list())
    print(s_2.to_list())
    print(s_l.to_list())


def f10():
    idx = [choice([1, 3, 5, 7]) for _ in range(10)]
    print(idx)
    shuffle(idx)
    print('shuffled: ', idx)
    s = pd.Series(idx)
    shuffle(s)
    print(s)


def f11():
    s = pd.Series(randint(-10, 10) for _ in range(75))
    print(s.to_list())
    s_sliced = s.apply(sign)
    s_zero = s_sliced[s_sliced == 'Zero']
    print(s_zero, '\n Count: ', len(s_zero))


def f12():
    s = pd.Series(randint(-10, 10) for _ in range(75))
    print(s.to_list())
    s_sliced = s.map(sign)
    s_zero = s_sliced[s_sliced == 'Zero']
    print(s_zero, '\n Count: ', len(s_zero))


def sign(x):
    if x > 0:
        return 'Positive'
    if x == 0:
        return 'Zero'
    if x < 0:
        return 'Negative'


if __name__ == '__main__':
    # pickle_file = '..\\input\\df_artists.pickle'
    # f1(pickle_file)
    # f2()
    # f3()
    # f4()
    # f5()
    f12()
    print('\ndone')
