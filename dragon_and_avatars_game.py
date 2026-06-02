from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class Avatar:
    health: int
    attack: int


@dataclass(frozen=True)
class GameResult:
    dragon_won: bool
    avatars_defeated: int
    dragon_health_left: int


def _validate_positive(name: str, value: int) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be greater than 0")


def simulate_game(
    dragon_health: int,
    dragon_attack: int,
    avatars: Sequence[Avatar] | Iterable[Avatar],
) -> GameResult:
    """Simulate a dragon fighting avatars one-by-one.

    The dragon and current avatar attack in alternating turns:
    - Dragon attacks first in every duel.
    - If the avatar survives, it retaliates once.

    The dragon wins only if it defeats every avatar in order.
    """
    _validate_positive("dragon_health", dragon_health)
    _validate_positive("dragon_attack", dragon_attack)

    health_left = dragon_health
    defeated = 0

    for avatar in avatars:
        _validate_positive("avatar.health", avatar.health)
        _validate_positive("avatar.attack", avatar.attack)
        avatar_health = avatar.health

        while avatar_health > 0 and health_left > 0:
            avatar_health -= dragon_attack
            if avatar_health > 0:
                health_left -= avatar.attack

        if health_left <= 0:
            return GameResult(False, defeated, 0)

        defeated += 1

    return GameResult(True, defeated, health_left)


def can_dragon_win(dragon_health: int, dragon_attack: int, avatars: Sequence[Avatar]) -> bool:
    return simulate_game(dragon_health, dragon_attack, avatars).dragon_won


def solve() -> None:
    """CLI entry point.

    Input:
      line 1: dragon_health dragon_attack
      line 2: number_of_avatars
      next n lines: avatar_health avatar_attack

    Output:
      DRAGON  -> dragon defeats all avatars
      AVATARS -> dragon is defeated
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    dragon_health = int(next(it))
    dragon_attack = int(next(it))
    total_avatars = int(next(it))

    avatars = []
    for _ in range(total_avatars):
        avatars.append(Avatar(int(next(it)), int(next(it))))

    print("DRAGON" if can_dragon_win(dragon_health, dragon_attack, avatars) else "AVATARS")


if __name__ == "__main__":
    solve()
