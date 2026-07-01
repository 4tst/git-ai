import json
import time
import functools
from pathlib import Path
from typing import Any, Callable
from collections.abc import Iterable


class Timer:
    """Context manager for measuring execution time."""

    def __init__(self, label: str = ""):
        self.label = label
        self.elapsed = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.elapsed = time.perf_counter() - self.start
        if self.label:
            print(f"{self.label}: {self.elapsed:.4f}s")


def retry(max_attempts: int = 3, delay: float = 0.5):
    """Decorator to retry a function on failure."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator


def chunked(iterable: Iterable, size: int) -> Iterable[list]:
    """Yield successive chunks of *size* from an iterable."""
    it = iter(iterable)
    while True:
        chunk = []
        for _ in range(size):
            try:
                chunk.append(next(it))
            except StopIteration:
                if chunk:
                    yield chunk
                return
        yield chunk


def json_load(path: str | Path, default: Any = None) -> Any:
    """Safely load JSON file, return *default* on missing/parse error."""
    path = Path(path)
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return default


def json_dump(path: str | Path, data: Any, **kwargs) -> None:
    """Atomically write JSON to file."""
    path = Path(path)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, **kwargs), encoding="utf-8")
    tmp.replace(path)


def flatten(nested: Iterable[Iterable]) -> list:
    """Flatten one level of nesting."""
    return [item for sub in nested for item in sub]


def unique_by(seq: Iterable, key: Callable) -> list:
    """Deduplicate by key function, preserving order."""
    seen = set()
    result = []
    for item in seq:
        k = key(item)
        if k not in seen:
            seen.add(k)
            result.append(item)
    return result


def singleton(cls: type) -> Callable:
    instances: dict = {}

    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


def group_by(seq: Iterable, key: Callable) -> dict:
    result = {}
    for item in seq:
        k = key(item)
        result.setdefault(k, []).append(item)
    return result


def deep_merge(base: dict, overlay: dict) -> dict:
    merged = base.copy()
    for k, v in overlay.items():
        if k in merged and isinstance(merged[k], dict) and isinstance(v, dict):
            merged[k] = deep_merge(merged[k], v)
        else:
            merged[k] = v
    return merged


if __name__ == "__main__":
    with Timer("test"):
        print(flatten([[1, 2], [3], [4, 5, 6]]))
        print(list(chunked(range(10), 3)))
        print(unique_by([{"id": 1}, {"id": 2}, {"id": 1}], key=lambda x: x["id"]))
        print(group_by(["apple", "banana", "avocado", "blueberry"], key=lambda s: s[0]))
        print(deep_merge({"a": 1, "b": {"c": 2}}, {"b": {"d": 3}, "e": 4}))
