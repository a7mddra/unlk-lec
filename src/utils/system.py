import sys
import os
from pathlib import Path

class SystemUtils:
    @staticmethod
    def get_documents_path():
        """Returns the user's Documents folder safely."""
        path = Path.home() / "Documents"
        
        if not path.exists():
            onedrive_path = Path.home() / "OneDrive" / "Documents"
            if onedrive_path.exists():
                return onedrive_path

        if not path.exists():
            return Path(os.getcwd())
                
        return path