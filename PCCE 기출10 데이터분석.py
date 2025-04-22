def solution(data, ext, val_ext, sort_by):
    col_dict = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    ext_idx = col_dict[ext]
    sort_idx = col_dict[sort_by]
    filtered_data = [d for d in data if d[ext_idx] < val_ext]
    sorted_data = sorted(filtered_data, key=lambda x: x[sort_idx])
    return sorted_data