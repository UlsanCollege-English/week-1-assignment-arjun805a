from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import Optional, TypeVar

T = TypeVar("T")


def add(a: int, b: int) -> int:
    return a + b


def is_even(n: int) -> bool:
    return n % 2 == 0


def linear_search(nums: Sequence[T], target: T) -> Optional[int]:
    for i, value in enumerate(nums):
        if value == target:
            return i
    return None


def count_occurrences(items: Iterable[T], target: T) -> int:
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count


# Stretch (optional)
def last_index(nums: Sequence[T], target: T) -> Optional[int]:
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == target:
            return i
    return None