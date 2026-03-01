from typing import List, TypeVar

def positifs_croissants[T](x: List[T]) -> List[T]:
    # On garde d'abord juste les positifs et puis on trie grâce à sorted
    return sorted([i for i in x if i >= 0])