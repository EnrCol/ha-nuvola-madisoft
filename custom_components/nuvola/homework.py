"""Normalize Nuvola homework descriptions without assuming their JSON shape."""

from __future__ import annotations

from typing import Any


_TEXT_FIELDS = (
    "testo",
    "descrizione",
    "descrizioneCompito",
    "testoCompito",
    "contenuto",
    "compito",
    "valore",
)


def _description_text(value: Any, *, depth: int = 0) -> str | None:
    """Turn known text/list/dict shapes into readable text, never repr(data)."""
    if depth > 5 or value is None:
        return None

    if isinstance(value, str):
        return value.strip() or None

    if isinstance(value, (list, tuple)):
        pieces = [
            text
            for item in value
            if (text := _description_text(item, depth=depth + 1))
        ]
        return "\n".join(pieces) or None

    if isinstance(value, dict):
        for key in _TEXT_FIELDS:
            if key in value:
                text = _description_text(value[key], depth=depth + 1)
                if text:
                    return text

    return None


def homework_description(item: dict[str, Any]) -> str | None:
    """Prefer existing valid descriptions, then Nuvola's descrizioneCompito."""
    return (
        _description_text(item.get("descrizione"))
        or _description_text(item.get("descrizioneCompito"))
    )
