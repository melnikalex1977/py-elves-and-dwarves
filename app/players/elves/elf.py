from app.players.player import Player
from abc import ABC, abstractmethod


class Elf(Player, ABC):
    def __init__(self, musical_instrument: int) -> str:
        self.musical_instrument = musical_instrument

    @abstractmethod
    def play_elf_song(self) -> str:
        print(f"{self.nickname} is playing a song on the "
              f"{self.musical_instrument}")