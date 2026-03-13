"""Type definitions for the BitBlock module."""

from typing import TypeIs, Union, Optional

type InputData = Union[int, bytes]

def is_valid_input_data(data: InputData, block_size: int) -> TypeIs[InputData]:
    """Check if the input data is valid for the given block size.
    
    Args:
        data: The input data to check (can be an integer or bytes).
        block_size: The size of the block in bits.
    
    Returns:
        True if the data is valid, False otherwise.
    """
    if isinstance(data, int):
        return True
    if isinstance(data, bytes) and len(data) <= block_size:
        return True
    return False

def is_valid_block_size(block_size: int) -> TypeIs[int]:
    """Check if the block size is valid (must be a positive multiple of 8).

    Args:
        block_size: The size of the block in bits.
    
    Returns:
        True if the block size is valid, False otherwise.
    """
    if block_size > 0 and block_size % 8 == 0:
        return True
    return False