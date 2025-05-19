from .nodes import SearchCSVByRow, WriteCSVByRow

NODE_CLASS_MAPPINGS = {
    "SearchCSVByRow": SearchCSVByRow,
    "WriteCSVByRow": WriteCSVByRow,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SearchCSVByRow": "Search CSV by Row",
    "WriteCSVByRow": "Write CSV by Row",
}

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]
