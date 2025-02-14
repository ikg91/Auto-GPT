"""Code evaluation module."""
from __future__ import annotations

from typing import TYPE_CHECKING

from autogpt.commands.command import command
from autogpt.llm.utils import call_ai_function

if TYPE_CHECKING:
    from autogpt.config import Config

if TYPE_CHECKING:
    from autogpt.config import Config


@command(
    "analyze_code",
    "Analyze Code",
    '"code": "<full_code_string>"',
)
def analyze_code(code: str, config: Config) -> list[str]:
    """
    A function that takes in a string and returns a response from create chat
      completion api call.

    Parameters:
        code (str): Code to be evaluated.
    Returns:
        A result string from create chat completion. A list of suggestions to
            improve the code.
    """

    function_string = "def analyze_code(code: str) -> list[str]:"
    args = [code]
    description_string = (
        "Analyzes the given code and returns a list of suggestions for improvements."
    )

    return call_ai_function(function_string, args, description_string, config=config)
