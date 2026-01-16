from dataclasses import dataclass


@dataclass
class Irasas:
    suma: int


@dataclass
class IslaiduIrasas(Irasas):
    isigyta: str
    info: str


@dataclass
class PajamuIrasas(Irasas):
    siuntejas: str
    info: str
