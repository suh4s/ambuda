"""Manages various small template filters."""

from datetime import datetime

from dateutil.relativedelta import relativedelta
from indic_transliteration import sanscript
from markdown_it import MarkdownIt


MARKDOWN = MarkdownIt()


def slp_to_devanagari(s: str) -> str:
    """SLP1 to Devanagari."""
    return sanscript.transliterate(s, sanscript.SLP1, sanscript.DEVANAGARI)


def devanagari(s: str) -> str:
    """HK to Devanagari."""
    return sanscript.transliterate(s, sanscript.HK, sanscript.DEVANAGARI)


def roman(s: str) -> str:
    """HK to Roman."""
    return sanscript.transliterate(s, sanscript.HK, sanscript.IAST)


def time_ago(dt: datetime, now=None) -> str:
    """Print a datetime relative to right now.

    :param dt: the datetime to check
    :param now: the "now" datetime. If not set, use `utcnow()`.
    """
    now = now or datetime.utcnow()
    rd = relativedelta(now, dt)
    for name in ["years", "months", "days", "hours", "minutes", "seconds"]:
        n = getattr(rd, name)
        if n:
            if n == 1:
                name = name[:-1]
            return f"{n} {name} ago"
    return "now"


def markdown(text: str) -> str:
    """Render the given Markdown text as HTML."""
    return MARKDOWN.render(text)
