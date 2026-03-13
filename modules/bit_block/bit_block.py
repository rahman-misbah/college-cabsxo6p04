from typing import Optional, TypeIs
import _bit_block_types as types

class BitBlock:
    """A class representing a block of bits.
    
    Attributes:
        block_size (int): The size of the block in bits.
        data (int): The data stored in the block as an integer.
    """
    def __init__(self, block_size: int, data: Optional[types.RawData] = None):
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
        if not is_valid_block_size(block_size):
            raise ValueError("Block size must be a positive integer and a multiple of 8.")
        
        self.__block_size = block_size

        # Validate data
        if not types.is_valid_raw_data(data, block_size):
            raise ValueError("Data must be an integer or bytes with length less than or equal to block size.")
        
        self.__data = _set_data(data)

        # Generate a mask to ensure data fits within the block size
        self.__mask = (1 << block_size) - 1
        self.__data &= self.__mask  # Ensure data fits within the block size
    
    def __repr__(self) -> str:
        return f"BitBlock(block_size={self.__block_size}, data={self.__data})"
    
    def __getitem__(self, position: int) -> int:
        """Get the value of the bit at the specified position using indexing syntax."""
        return self.get_bit(position)
    
    def __lshift__(self, other: int):
        """Left shift the bits in the block by the specified number of positions."""
        if not isinstance(other, int):
            raise ValueError("Shift amount must be an integer.")
        self.__data = (self.__data << other) & self.__mask
        return self
    
    def __rshift__(self, other: int):
        """Right shift the bits in the block by the specified number of positions."""
        if not isinstance(other, int):
            raise ValueError("Shift amount must be an integer.")
        self.__data = (self.__data >> other) & self.__mask
        return self
    
    

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
    
    def get_bit(self, position: int) -> int:
        """Get the value of the bit at the specified position.

        Args:
            position: The position of the bit to get (0-indexed from the right).

        Returns:
            The value of the bit at the specified position (0 or 1).

        Raises:
            IndexError: If position is negative or greater than or equal to block_size.
        """
        if not _is_valid_position(position, self.__block_size):
            raise IndexError("Position must be within the block size.")
        return (self.__data >> position) & 1
    
    def set_bit(self, position: int) -> None:
        """Set the bit at the specified position to 1.

        Args:
            position: The position of the bit to set (0-indexed from the right).

        Raises:
            IndexError: If position is negative or greater than or equal to block_size.
        """
        if not _is_valid_position(position, self.__block_size):
            raise IndexError("Position must be within the block size.")
        self.__data |= (1 << position)
    
    def clear_bit(self, position: int) -> None:
        """Clear the bit at the specified position to 0.

        Args:
            position: The position of the bit to clear (0-indexed from the right).

        Raises:
            IndexError: If position is negative or greater than or equal to block_size.
        """
        if not _is_valid_position(position, self.__block_size):
            raise IndexError("Position must be within the block size.")
        self.__data &= ~(1 << position)
    
    def toggle_bit(self, position: int) -> None:
        """Toggle the bit at the specified position.

        Args:
            position: The position of the bit to toggle (0-indexed from the right).

        Raises:
            IndexError: If position is negative or greater than or equal to block_size.
        """
        if not _is_valid_position(position, self.__block_size):
            raise IndexError("Position must be within the block size.")
        self.__data ^= (1 << position)

# Helper Functions
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

def _set_data(data: Optional[types.RawData]) -> int:
    """Convert the input data to an integer."""
    if data is None:
        return 0
    if isinstance(data, int):
        return data
    if isinstance(data, bytes):
        return int.from_bytes(data, byteorder='big')

def _is_valid_position(position: int, block_size: int) -> bool:
    """Check if the position is valid for the given block size."""
    return 0 <= position < block_size