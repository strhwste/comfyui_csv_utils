from .nodes import SearchCSVByRow, WriteCSVByRow, ExtractFromJSON

NODE_CLASS_MAPPINGS = {
    "SearchCSVByRow": SearchCSVByRow,
    "WriteCSVByRow": WriteCSVByRow,
    "ExtractFromJSON": ExtractFromJSON,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SearchCSVByRow": "Search CSV by Row",
    "WriteCSVByRow": "Write CSV by Row",
    "ExtractFromJSON": "Extract from JSON",
}

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]
