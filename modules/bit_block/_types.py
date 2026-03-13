from typing import TypeIs, Union

type Data = Union[int, bytes]

def is_valid_data(data: Data, block_size: int) -> TypeIs[Data]:
    if isinstance(data, int):
        return True
    if isinstance(data, bytes) and len(data) <= block_size:
        return True
    return False

def is_valid_block_size(block_size: int) -> TypeIs[int]:
    if block_size > 0 and block_size % 8 == 0:
        return True
    return False