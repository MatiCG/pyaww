# Related third party imports

import pytest

# Local application/library specific imports

from pyaww import Console


@pytest.mark.asyncio
async def test_send_input(
    started_console: Console,
) -> None:  # this method also tests pyaww.Console.outputs()
    assert isinstance(await started_console.send_input("echo hello!"), str)


@pytest.mark.asyncio
async def test_delete(unstarted_console: Console) -> None:  # cleanup + test
    assert await unstarted_console.delete() is None
