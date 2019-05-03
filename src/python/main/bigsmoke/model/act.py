from dataclasses import dataclass
from typing import Optional


@dataclass
class Act:
    name: str
    alias: Optional[str] = None

    def performing_as(self, alias: str) -> "Act":
        return Act(name=self.name, alias=alias)
