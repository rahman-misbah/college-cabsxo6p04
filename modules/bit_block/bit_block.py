from typing import Optional
from . import _types

class BitBlock:
    """A class representing a block of bits.
    
    Attributes:
        block_size (int): The size of the block in bits.
        data (int): The data stored in the block as an integer.
    """
    def __init__(self, block_size: int, data: Optional[_types.Data] = None):
        """Initialize a BitBlock instance.

        Args:
            block_size: The size of the block in bits. Must be a positive integer and a multiple of 8.
            data: The data to be stored in the block. Can be an integer or bytes. 
                  If bytes, its length must be less than or equal to block_size // 8.
        
        Raises:
            ValueError: If block_size is not a positive integer or not a multiple of 8
                        If data is not an integer or bytes, or if bytes length exceeds block_size // 8.
        """
        
        # Validate block_size
        if not _types.is_valid_block_size(block_size):
            raise ValueError("Block size must be a positive integer and a multiple of 8.")
        
        self.__block_size = block_size

        # Validate data
        if not _types.is_valid_data(data, block_size):
            raise ValueError("Data must be an integer or bytes with length less than or equal to block size.")
        
        self.__data = self._set_data(data)
        
    
    # GETTERS AND SETTERS

    @property
    def block_size(self) -> int:
        return self.__block_size
    
    @property
    def data(self) -> int:
        return self.__data
    
    # PUBLIC METHODS

    def to_bytes(self) -> bytes:
        return self.__data.to_bytes(self.__block_size // 8, byteorder='big')
    
    def set_bit(self, position: int) -> None:
        """Set the bit at the specified position to 1.

        Args:
            position: The position of the bit to set (0-indexed from the right).

        Raises:
            ValueError: If position is negative or greater than or equal to block_size.
        """
        if position < 0 or position >= self.__block_size:
            raise ValueError("Position must be within the block size.")
        self.__data |= (1 << position)
    
    def clear_bit(self, position: int) -> None:
        """Clear the bit at the specified position to 0.

        Args:
            position: The position of the bit to clear (0-indexed from the right).

        Raises:
            ValueError: If position is negative or greater than or equal to block_size.
        """
        if position < 0 or position >= self.__block_size:
            raise ValueError("Position must be within the block size.")
        self.__data &= ~(1 << position)
    
    def toggle_bit(self, position: int) -> None:
        """Toggle the bit at the specified position.

        Args:
            position: The position of the bit to toggle (0-indexed from the right).

        Raises:
            ValueError: If position is negative or greater than or equal to block_size.
        """
        if position < 0 or position >= self.__block_size:
            raise ValueError("Position must be within the block size.")
        self.__data ^= (1 << position)

# Helper Functions
def _set_data(self, data: Optional[_types.Data]) -> int:
    if data is None:
        return 0
    if isinstance(data, int):
        return data
    if isinstance(data, bytes):
        return int.from_bytes(data, byteorder='big')