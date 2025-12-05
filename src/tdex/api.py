"""CLI wrapper around `aiopoke` objects."""

import aiopoke
from cyclopts import App

from tdex.console import console

sub_app = App()


@sub_app.command(group="Ability")
async def ability(name: str, /) -> None:
    """
    Get `Abiltiy`.

    Args:
        name (str): Ability name

    """
    async with aiopoke.AiopokeClient() as client:
        ability = await client.get_ability(name)

    console.print(ability)
