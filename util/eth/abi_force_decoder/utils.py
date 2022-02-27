from itertools import permutations, product


def fn_signature_compose(names: [str], arg_sigs: [str]):
    """组合生成不重复的函数签名: fn_signature_compose(['mint', 'claim'], ['uint num', 'uint256 num'])"""
    transformed_names = []
    for name in names:
        n = str(name).replace(' ', '')
        transformed_names.append(n)
        n = str(name).lower().replace(' ', '')
        transformed_names.append(n)
        n = str(name).title().replace(' ', '')
        transformed_names.append(n)

    transformed_names = list(set(transformed_names))
    transformed_names.sort()
    # print(transformed_names)

    items = product(transformed_names, arg_sigs)
    for item in items:
        line = f'{item[0]}({item[1]})'
        yield line