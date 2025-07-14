import os

def get_project_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def from_root(*parts):
    """Build an absolute path from project root."""
    return os.path.join(get_project_root(), *parts)